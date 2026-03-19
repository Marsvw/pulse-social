from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User, Post, Comment
from app.schemas import UserOut, AdminUserUpdate, AdminStats
from app.auth import require_admin

router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.get("/stats", response_model=AdminStats)
async def admin_stats(db: AsyncSession = Depends(get_db), admin: User = Depends(require_admin)):
    users = (await db.execute(select(func.count(User.id)))).scalar() or 0
    posts = (await db.execute(select(func.count(Post.id)))).scalar() or 0
    comments = (await db.execute(select(func.count(Comment.id)))).scalar() or 0
    return AdminStats(total_users=users, total_posts=posts, total_comments=comments)


@router.get("/users", response_model=list[UserOut])
async def list_users(db: AsyncSession = Depends(get_db), admin: User = Depends(require_admin)):
    result = await db.execute(select(User).order_by(User.created_at.desc()))
    return result.scalars().all()


@router.patch("/users/{user_id}", response_model=UserOut)
async def update_user(
    user_id: int,
    payload: AdminUserUpdate,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(user, key, val)
    await db.commit()
    await db.refresh(user)
    return user


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.id == admin.id:
        raise HTTPException(status_code=400, detail="Cannot delete yourself")
    await db.delete(user)
    await db.commit()


@router.delete("/posts/{post_id}", status_code=204)
async def admin_delete_post(
    post_id: int,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    post = await db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await db.delete(post)
    await db.commit()
