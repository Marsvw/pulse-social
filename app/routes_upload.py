import csv
import io
import re
import datetime
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User, Transaction, Upload, Account
from app.schemas import UploadOut
from app.auth import require_user

router = APIRouter(prefix="/api/upload", tags=["upload"])

# Common date formats to try
DATE_FORMATS = [
    "%m/%d/%Y", "%Y-%m-%d", "%m-%d-%Y", "%d/%m/%Y",
    "%m/%d/%y", "%d-%m-%Y", "%Y/%m/%d", "%m.%d.%Y",
    "%d.%m.%Y", "%b %d, %Y", "%B %d, %Y",
]


def parse_date(s: str) -> datetime.date | None:
    s = s.strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def parse_amount(s: str) -> float | None:
    s = s.strip().replace(",", "").replace("$", "").replace("€", "").replace("£", "")
    # Handle parenthetical negatives: (123.45) -> -123.45
    if s.startswith("(") and s.endswith(")"):
        s = "-" + s[1:-1]
    try:
        return float(s)
    except ValueError:
        return None


def guess_category(desc: str) -> str:
    desc_lower = desc.lower()
    categories = {
        "Groceries": ["grocery", "supermarket", "walmart", "costco", "trader joe", "whole foods", "aldi", "kroger", "safeway", "publix", "target"],
        "Dining": ["restaurant", "mcdonald", "starbucks", "chipotle", "subway", "pizza", "burger", "cafe", "coffee", "doordash", "uber eats", "grubhub", "taco"],
        "Gas & Auto": ["shell", "chevron", "exxon", "gas", "fuel", "auto", "car wash", "parking", "oil change"],
        "Shopping": ["amazon", "ebay", "etsy", "best buy", "apple.com", "nike", "clothing", "mall"],
        "Subscriptions": ["netflix", "spotify", "hulu", "disney", "hbo", "youtube", "apple music", "adobe", "microsoft", "openai", "chatgpt", "icloud", "dropbox", "notion"],
        "Utilities": ["electric", "water", "gas bill", "internet", "comcast", "att", "verizon", "t-mobile", "phone bill", "utility"],
        "Housing": ["rent", "mortgage", "hoa", "property tax", "home insurance"],
        "Insurance": ["insurance", "geico", "progressive", "state farm", "allstate"],
        "Health": ["pharmacy", "cvs", "walgreens", "doctor", "hospital", "dental", "medical", "health"],
        "Transport": ["uber", "lyft", "transit", "metro", "bus", "train", "airline", "flight", "delta", "united", "southwest"],
        "Entertainment": ["movie", "theater", "concert", "ticket", "gaming", "steam", "playstation", "xbox"],
        "Income": ["payroll", "salary", "direct dep", "deposit", "refund", "reimbursement", "interest", "dividend"],
        "Transfer": ["transfer", "zelle", "venmo", "paypal", "cash app", "wire"],
    }
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in desc_lower:
                return cat
    return "Uncategorized"


def detect_csv_columns(headers: list[str]) -> dict:
    """Try to map CSV headers to our fields: date, description, amount, debit, credit."""
    mapping = {}
    headers_lower = [h.strip().lower() for h in headers]

    date_words = ["date", "posted", "transaction date", "posting date"]
    desc_words = ["description", "memo", "payee", "merchant", "name", "details", "narrative"]
    amount_words = ["amount", "total"]
    debit_words = ["debit", "withdrawal", "charge"]
    credit_words = ["credit", "deposit", "payment"]

    for i, h in enumerate(headers_lower):
        if not mapping.get("date") and any(w in h for w in date_words):
            mapping["date"] = i
        elif not mapping.get("description") and any(w in h for w in desc_words):
            mapping["description"] = i
        elif not mapping.get("amount") and any(w in h for w in amount_words):
            mapping["amount"] = i
        elif not mapping.get("debit") and any(w in h for w in debit_words):
            mapping["debit"] = i
        elif not mapping.get("credit") and any(w in h for w in credit_words):
            mapping["credit"] = i

    return mapping


@router.post("/csv", response_model=UploadOut)
async def upload_csv(
    file: UploadFile = File(...),
    account_id: int | None = Form(default=None),
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files accepted")

    content = await file.read()
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        text = content.decode("latin-1")

    reader = csv.reader(io.StringIO(text))
    rows = list(reader)
    if len(rows) < 2:
        raise HTTPException(status_code=400, detail="CSV has no data rows")

    headers = rows[0]
    mapping = detect_csv_columns(headers)

    if "date" not in mapping or "description" not in mapping:
        raise HTTPException(
            status_code=400,
            detail=f"Could not detect date/description columns. Headers found: {headers}"
        )

    upload = Upload(
        user_id=user.id,
        filename=file.filename,
        file_type="csv",
        status="processing",
    )
    db.add(upload)
    await db.flush()

    count = 0
    errors = []
    for row_num, row in enumerate(rows[1:], start=2):
        if not row or all(c.strip() == "" for c in row):
            continue
        try:
            date = parse_date(row[mapping["date"]])
            desc = row[mapping["description"]].strip()
            if not date or not desc:
                errors.append(f"Row {row_num}: missing date or description")
                continue

            # Determine amount
            if "amount" in mapping:
                amt = parse_amount(row[mapping["amount"]])
            elif "debit" in mapping and "credit" in mapping:
                debit = parse_amount(row[mapping["debit"]]) if row[mapping["debit"]].strip() else None
                credit = parse_amount(row[mapping["credit"]]) if row[mapping["credit"]].strip() else None
                if debit:
                    amt = -abs(debit)
                elif credit:
                    amt = abs(credit)
                else:
                    errors.append(f"Row {row_num}: no amount found")
                    continue
            else:
                errors.append(f"Row {row_num}: no amount column")
                continue

            if amt is None:
                errors.append(f"Row {row_num}: could not parse amount")
                continue

            txn = Transaction(
                user_id=user.id,
                account_id=account_id,
                date=date,
                description=desc,
                amount=amt,
                category=guess_category(desc),
                source="csv",
                upload_id=upload.id,
            )
            db.add(txn)
            count += 1
        except (IndexError, ValueError) as e:
            errors.append(f"Row {row_num}: {str(e)}")

    upload.row_count = count
    upload.status = "processed" if count > 0 else "error"
    if errors:
        upload.error_message = "; ".join(errors[:10])
    await db.commit()
    await db.refresh(upload)
    return upload


@router.post("/pdf", response_model=UploadOut)
async def upload_pdf(
    file: UploadFile = File(...),
    account_id: int | None = Form(default=None),
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files accepted")

    content = await file.read()

    upload = Upload(
        user_id=user.id,
        filename=file.filename,
        file_type="pdf",
        status="processing",
    )
    db.add(upload)
    await db.flush()

    try:
        import subprocess
        import tempfile
        import os

        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        # Use pdftotext if available, fallback to basic extraction
        try:
            result = subprocess.run(
                ["pdftotext", "-layout", tmp_path, "-"],
                capture_output=True, text=True, timeout=30
            )
            text = result.stdout
        except FileNotFoundError:
            # Fallback: try to extract text with a simple approach
            text = content.decode("latin-1", errors="ignore")
        finally:
            os.unlink(tmp_path)

        # Parse text for transaction-like patterns
        # Pattern: date  description  amount
        date_pattern = re.compile(
            r'(\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4})\s+'
            r'(.+?)\s+'
            r'(-?\$?[\d,]+\.?\d{0,2})\s*$',
            re.MULTILINE
        )

        count = 0
        for match in date_pattern.finditer(text):
            date = parse_date(match.group(1))
            desc = match.group(2).strip()
            amt = parse_amount(match.group(3))

            if date and desc and amt is not None:
                txn = Transaction(
                    user_id=user.id,
                    account_id=account_id,
                    date=date,
                    description=desc,
                    amount=amt,
                    category=guess_category(desc),
                    source="pdf",
                    upload_id=upload.id,
                )
                db.add(txn)
                count += 1

        upload.row_count = count
        upload.status = "processed" if count > 0 else "error"
        if count == 0:
            upload.error_message = "Could not extract transactions from PDF. Try CSV instead for best results."

    except Exception as e:
        upload.status = "error"
        upload.error_message = f"PDF processing error: {str(e)}"

    await db.commit()
    await db.refresh(upload)
    return upload


@router.get("/history", response_model=list[UploadOut])
async def upload_history(user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Upload).where(Upload.user_id == user.id).order_by(Upload.created_at.desc()).limit(50)
    )
    return result.scalars().all()
