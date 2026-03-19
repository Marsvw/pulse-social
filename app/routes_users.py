from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models import User, Post, Comment, Like
from app.schemas import UserOut, UserUpdate, PostOut
from app.auth import get_current_user, require_user
from app.routes_posts import post_to_out

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/{username}", response_model=UserOut)
async def get_profile(username: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch("/me", response_model=UserOut)
async def update_my_profile(
    payload: UserUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(user, key, val)
    await db.commit()
    await db.refresh(user)
    return user


@router.get("/{username}/posts", response_model=list[PostOut])
async def get_user_posts(
    username: str,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    result = await db.execute(select(User).where(User.username == username))
    profile_user = result.scalars().first()
    if not profile_user:
        raise HTTPException(status_code=404, detail="User not found")

    result = await db.execute(
        select(Post)
        .options(
            selectinload(Post.author),
            selectinload(Post.comments).selectinload(Comment.author),
            selectinload(Post.likes),
        )
        .where(Post.author_id == profile_user.id)
        .order_by(Post.created_at.desc())
    )
    posts = result.scalars().unique().all()
    uid = current_user.id if current_user else None
    return [post_to_out(p, uid) for p in posts]
