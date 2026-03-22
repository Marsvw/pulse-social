import datetime
from fastapi import APIRouter, Depends, Query
from sqlalchemy import select, func, extract, case, and_, distinct
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User, Transaction, Account
from app.auth import require_user

router = APIRouter(prefix="/api/analytics", tags=["analytics"])


@router.get("/overview")
async def overview(user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    """Big-picture stats: total income, expenses, net, account balances."""
    today = datetime.date.today()
    month_start = today.replace(day=1)

    # This month's totals
    result = await db.execute(
        select(
            func.coalesce(func.sum(case((Transaction.amount > 0, Transaction.amount), else_=0)), 0).label("income"),
            func.coalesce(func.sum(case((Transaction.amount < 0, Transaction.amount), else_=0)), 0).label("expenses"),
            func.count(Transaction.id).label("txn_count"),
        ).where(
            Transaction.user_id == user.id,
            Transaction.date >= month_start,
            Transaction.date <= today,
        )
    )
    row = result.one()
    income = float(row.income)
    expenses = float(row.expenses)

    # Last month for comparison
    last_month_end = month_start - datetime.timedelta(days=1)
    last_month_start = last_month_end.replace(day=1)
    result2 = await db.execute(
        select(
            func.coalesce(func.sum(case((Transaction.amount > 0, Transaction.amount), else_=0)), 0).label("income"),
            func.coalesce(func.sum(case((Transaction.amount < 0, Transaction.amount), else_=0)), 0).label("expenses"),
        ).where(
            Transaction.user_id == user.id,
            Transaction.date >= last_month_start,
            Transaction.date <= last_month_end,
        )
    )
    prev = result2.one()

    # Account balances
    accts = await db.execute(
        select(Account).where(Account.user_id == user.id, Account.is_active == True)
    )
    accounts = accts.scalars().all()
    total_balance = sum(a.balance for a in accounts)

    # All-time totals
    all_result = await db.execute(
        select(
            func.coalesce(func.sum(case((Transaction.amount > 0, Transaction.amount), else_=0)), 0),
            func.coalesce(func.sum(case((Transaction.amount < 0, Transaction.amount), else_=0)), 0),
            func.count(Transaction.id),
        ).where(Transaction.user_id == user.id)
    )
    all_row = all_result.one()

    return {
        "this_month": {
            "income": round(income, 2),
            "expenses": round(abs(expenses), 2),
            "net": round(income + expenses, 2),
            "txn_count": row.txn_count,
        },
        "last_month": {
            "income": round(float(prev.income), 2),
            "expenses": round(abs(float(prev.expenses)), 2),
        },
        "all_time": {
            "income": round(float(all_row[0]), 2),
            "expenses": round(abs(float(all_row[1])), 2),
            "net": round(float(all_row[0]) + float(all_row[1]), 2),
            "txn_count": all_row[2],
        },
        "total_balance": round(total_balance, 2),
        "account_count": len(accounts),
    }


@router.get("/spending-by-category")
async def spending_by_category(
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
    months: int = Query(default=1, ge=1, le=24),
):
    since = datetime.date.today() - datetime.timedelta(days=months * 30)
    result = await db.execute(
        select(
            Transaction.category,
            func.sum(Transaction.amount).label("total"),
            func.count(Transaction.id).label("count"),
            func.avg(Transaction.amount).label("avg"),
        )
        .where(Transaction.user_id == user.id, Transaction.amount < 0, Transaction.date >= since)
        .group_by(Transaction.category)
        .order_by(func.sum(Transaction.amount))
    )
    return [
        {
            "category": r.category,
            "total": round(abs(float(r.total)), 2),
            "count": r.count,
            "avg": round(abs(float(r.avg)), 2),
        }
        for r in result.all()
    ]


@router.get("/monthly-trend")
async def monthly_trend(
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
    months: int = Query(default=12, ge=1, le=36),
):
    since = datetime.date.today() - datetime.timedelta(days=months * 30)
    result = await db.execute(
        select(
            extract("year", Transaction.date).label("year"),
            extract("month", Transaction.date).label("month"),
            func.sum(case((Transaction.amount > 0, Transaction.amount), else_=0)).label("income"),
            func.sum(case((Transaction.amount < 0, Transaction.amount), else_=0)).label("expenses"),
            func.count(Transaction.id).label("count"),
        )
        .where(Transaction.user_id == user.id, Transaction.date >= since)
        .group_by("year", "month")
        .order_by("year", "month")
    )
    return [
        {
            "year": int(r.year),
            "month": int(r.month),
            "income": round(float(r.income), 2),
            "expenses": round(abs(float(r.expenses)), 2),
            "net": round(float(r.income) + float(r.expenses), 2),
            "count": r.count,
        }
        for r in result.all()
    ]


@router.get("/subscriptions")
async def detect_subscriptions(
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Detect recurring charges by finding descriptions that appear 2+ times with similar amounts."""
    three_months_ago = datetime.date.today() - datetime.timedelta(days=90)
    result = await db.execute(
        select(
            Transaction.description,
            Transaction.category,
            func.count(Transaction.id).label("occurrences"),
            func.avg(Transaction.amount).label("avg_amount"),
            func.min(Transaction.date).label("first_seen"),
            func.max(Transaction.date).label("last_seen"),
        )
        .where(
            Transaction.user_id == user.id,
            Transaction.amount < 0,
            Transaction.date >= three_months_ago,
        )
        .group_by(Transaction.description, Transaction.category)
        .having(func.count(Transaction.id) >= 2)
        .order_by(func.avg(Transaction.amount))
    )

    subs = []
    for r in result.all():
        avg = abs(float(r.avg_amount))
        subs.append({
            "description": r.description,
            "category": r.category,
            "occurrences": r.occurrences,
            "avg_amount": round(avg, 2),
            "estimated_monthly": round(avg, 2),
            "estimated_yearly": round(avg * 12, 2),
            "first_seen": str(r.first_seen),
            "last_seen": str(r.last_seen),
        })
    return {
        "subscriptions": subs,
        "total_monthly": round(sum(s["estimated_monthly"] for s in subs), 2),
        "total_yearly": round(sum(s["estimated_yearly"] for s in subs), 2),
    }


@router.get("/daily-spending")
async def daily_spending(
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
    days: int = Query(default=30, ge=7, le=365),
):
    since = datetime.date.today() - datetime.timedelta(days=days)
    result = await db.execute(
        select(
            Transaction.date,
            func.sum(case((Transaction.amount < 0, Transaction.amount), else_=0)).label("spent"),
            func.sum(case((Transaction.amount > 0, Transaction.amount), else_=0)).label("earned"),
        )
        .where(Transaction.user_id == user.id, Transaction.date >= since)
        .group_by(Transaction.date)
        .order_by(Transaction.date)
    )
    return [
        {
            "date": str(r.date),
            "spent": round(abs(float(r.spent)), 2),
            "earned": round(float(r.earned), 2),
        }
        for r in result.all()
    ]


@router.get("/top-merchants")
async def top_merchants(
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
    months: int = Query(default=3, ge=1, le=12),
    limit: int = Query(default=15, le=50),
):
    since = datetime.date.today() - datetime.timedelta(days=months * 30)
    result = await db.execute(
        select(
            Transaction.description,
            Transaction.category,
            func.sum(Transaction.amount).label("total"),
            func.count(Transaction.id).label("count"),
        )
        .where(Transaction.user_id == user.id, Transaction.amount < 0, Transaction.date >= since)
        .group_by(Transaction.description, Transaction.category)
        .order_by(func.sum(Transaction.amount))
        .limit(limit)
    )
    return [
        {
            "merchant": r.description,
            "category": r.category,
            "total": round(abs(float(r.total)), 2),
            "count": r.count,
        }
        for r in result.all()
    ]
