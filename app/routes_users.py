import base64
import io

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.database import get_db
from app.models import User, Post, Comment, Like
from app.schemas import UserOut, UserUpdate, PostOut
from app.auth import get_current_user, require_user
from app.routes_posts import post_to_out

router = APIRouter(prefix="/api/users", tags=["users"])

AVATAR_MAX_SIZE = 200  # px
AVATAR_QUALITY = 80
AVATAR_MAX_BYTES = 5 * 1024 * 1024  # 5MB upload limit


# ── Static /me routes FIRST (before /{username} wildcard) ──

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


@router.post("/me/avatar", response_model=UserOut)
async def upload_avatar(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    # Validate file type
    if file.content_type not in ("image/jpeg", "image/png", "image/gif", "image/webp"):
        raise HTTPException(status_code=400, detail="Only JPEG, PNG, GIF, and WebP images are allowed")

    data = await file.read()
    if len(data) > AVATAR_MAX_BYTES:
        raise HTTPException(status_code=400, detail="Image must be under 5MB")

    try:
        from PIL import Image
        img = Image.open(io.BytesIO(data))
        img = img.convert("RGB")
        # Crop to square from center
        w, h = img.size
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 2
        img = img.crop((left, top, left + side, top + side))
        # Resize to thumbnail
        img = img.resize((AVATAR_MAX_SIZE, AVATAR_MAX_SIZE), Image.LANCZOS)
        # Encode as JPEG base64
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=AVATAR_QUALITY)
        b64 = base64.b64encode(buf.getvalue()).decode()
        data_url = f"data:image/jpeg;base64,{b64}"
    except ImportError:
        raise HTTPException(status_code=500, detail="Image processing library not available")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not process image: {str(e)}")

    user.avatar_url = data_url
    await db.commit()
    await db.refresh(user)
    return user


# ── Dynamic /{username} routes AFTER /me routes ──

@router.get("/{username}", response_model=UserOut)
async def get_profile(username: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
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
