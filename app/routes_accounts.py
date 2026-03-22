from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User, Account
from app.schemas import AccountCreate, AccountUpdate, AccountOut
from app.auth import require_user

router = APIRouter(prefix="/api/accounts", tags=["accounts"])


@router.get("/", response_model=list[AccountOut])
async def list_accounts(user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Account).where(Account.user_id == user.id, Account.is_active == True).order_by(Account.name)
    )
    return result.scalars().all()


@router.post("/", response_model=AccountOut, status_code=201)
async def create_account(payload: AccountCreate, user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    acct = Account(user_id=user.id, **payload.model_dump())
    db.add(acct)
    await db.commit()
    await db.refresh(acct)
    return acct


@router.put("/{account_id}", response_model=AccountOut)
async def update_account(account_id: int, payload: AccountUpdate, user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    acct = await db.get(Account, account_id)
    if not acct or acct.user_id != user.id:
        raise HTTPException(status_code=404, detail="Account not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(acct, k, v)
    await db.commit()
    await db.refresh(acct)
    return acct


@router.delete("/{account_id}")
async def delete_account(account_id: int, user: User = Depends(require_user), db: AsyncSession = Depends(get_db)):
    acct = await db.get(Account, account_id)
    if not acct or acct.user_id != user.id:
        raise HTTPException(status_code=404, detail="Account not found")
    acct.is_active = False
    await db.commit()
    return {"message": "Account archived"}
