from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession
import datetime

from app.database import get_db
from app.models import User, Transaction
from app.schemas import TransactionCreate, TransactionUpdate, TransactionOut
from app.auth import require_user

router = APIRouter(prefix="/api/transactions", tags=["transactions"])


@router.get("/", response_model=list[TransactionOut])
async def list_transactions(
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
    account_id: int | None = None,
    category: str | None = None,
    date_from: datetime.date | None = None,
    date_to: datetime.date | None = None,
    search: str | None = None,
    limit: int = Query(default=200, le=1000),
    offset: int = 0,
):
    q = select(Transaction).where(Transaction.user_id == user.id)
    if account_id:
        q = q.where(Transaction.account_id == account_id)
    if category:
        q = q.where(Transaction.category == category)
    if date_from:
        q = q.where(Transaction.date >= date_from)
    if date_to:
        q = q.where(Transaction.date <= date_to)
    if search:
        q = q.where(Transaction.description.ilike(f"%{search}%"))
    q = q.order_by(Transaction.date.desc(), Transaction.id.desc()).offset(offset).limit(limit)
    result = await db.execute(q)
    return result.scalars().all()


@router.post("/", response_model=TransactionOut, status_code=201)
async def create_transaction(payload: TransactionCreate, user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    txn = Transaction(user_id=user.id, source="manual", **payload.model_dump())
    db.add(txn)
    await db.commit()
    await db.refresh(txn)
    return txn


@router.put("/{txn_id}", response_model=TransactionOut)
async def update_transaction(txn_id: int, payload: TransactionUpdate, user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    txn = await db.get(Transaction, txn_id)
    if not txn or txn.user_id != user.id:
        raise HTTPException(status_code=404, detail="Transaction not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(txn, k, v)
    await db.commit()
    await db.refresh(txn)
    return txn


@router.delete("/{txn_id}")
async def delete_transaction(txn_id: int, user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    txn = await db.get(Transaction, txn_id)
    if not txn or txn.user_id != user.id:
        raise HTTPException(status_code=404, detail="Transaction not found")
    await db.delete(txn)
    await db.commit()
    return {"message": "Transaction deleted"}


@router.get("/categories")
async def list_categories(user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Transaction.category, func.count(Transaction.id), func.sum(Transaction.amount))
        .where(Transaction.user_id == user.id)
        .group_by(Transaction.category)
        .order_by(func.sum(Transaction.amount))
    )
    return [{"category": r[0], "count": r[1], "total": round(r[2], 2)} for r in result.all()]
