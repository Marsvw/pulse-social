from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models import User, Post, Comment, Like
from app.schemas import PostCreate, PostUpdate, PostOut, CommentCreate, CommentOut
from app.auth import get_current_user, require_user

router = APIRouter(prefix="/api/posts", tags=["posts"])


def post_to_out(post: Post, current_user_id: int | None = None) -> PostOut:
    liked_by_me = False
    if current_user_id:
        liked_by_me = any(like.user_id == current_user_id for like in post.likes)

    comments = []
    for c in sorted(post.comments, key=lambda x: x.created_at):
        comments.append(CommentOut(
            id=c.id,
            body=c.body,
            author_id=c.author_id,
            author_username=c.author.username if c.author else "",
            created_at=c.created_at,
        ))

    return PostOut(
        id=post.id,
        title=post.title,
        body=post.body,
        category=post.category or "discussion",
        link_url=post.link_url,
        author_id=post.author_id,
        author_username=post.author.username,
        author_display_name=post.author.display_name or post.author.username,
        author_avatar_url=post.author.avatar_url,
        like_count=post.like_count,
        liked_by_me=liked_by_me,
        comment_count=len(post.comments),
        comments=comments,
        created_at=post.created_at,
        updated_at=post.updated_at,
    )


@router.get("/", response_model=list[PostOut])
async def list_posts(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    category: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    offset = (page - 1) * limit
    query = select(Post).options(
        selectinload(Post.author),
        selectinload(Post.comments).selectinload(Comment.author),
        selectinload(Post.likes),
    )
    if category:
        query = query.where(Post.category == category)
    result = await db.execute(
        query.order_by(desc(Post.created_at))
        .offset(offset)
        .limit(limit)
    )
    posts = result.scalars().unique().all()
    uid = current_user.id if current_user else None
    return [post_to_out(p, uid) for p in posts]


@router.post("/", response_model=PostOut, status_code=201)
async def create_post(
    payload: PostCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    # Only admins (teachers) can post materials
    if payload.category == "material" and not user.is_admin:
        raise HTTPException(status_code=403, detail="Only the teacher can post materials")
    post = Post(
        title=payload.title,
        body=payload.body,
        category=payload.category,
        link_url=payload.link_url,
        author_id=user.id,
    )
    db.add(post)
    await db.commit()

    result = await db.execute(
        select(Post)
        .options(
            selectinload(Post.author),
            selectinload(Post.comments).selectinload(Comment.author),
            selectinload(Post.likes),
        )
        .where(Post.id == post.id)
    )
    post = result.scalars().first()
    return post_to_out(post, user.id)


@router.get("/{post_id}", response_model=PostOut)
async def get_post(
    post_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    result = await db.execute(
        select(Post)
        .options(
            selectinload(Post.author),
            selectinload(Post.comments).selectinload(Comment.author),
            selectinload(Post.likes),
        )
        .where(Post.id == post_id)
    )
    post = result.scalars().first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    uid = current_user.id if current_user else None
    return post_to_out(post, uid)


@router.patch("/{post_id}", response_model=PostOut)
async def update_post(
    post_id: int,
    payload: PostUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    post = await db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.author_id != user.id and not user.is_admin:
        raise HTTPException(status_code=403, detail="Not your post")

    for key, val in payload.model_dump(exclude_unset=True).items():
        setattr(post, key, val)
    await db.commit()

    result = await db.execute(
        select(Post)
        .options(
            selectinload(Post.author),
            selectinload(Post.comments).selectinload(Comment.author),
            selectinload(Post.likes),
        )
        .where(Post.id == post_id)
    )
    post = result.scalars().first()
    return post_to_out(post, user.id)


@router.delete("/{post_id}", status_code=204)
async def delete_post(
    post_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    post = await db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.author_id != user.id and not user.is_admin:
        raise HTTPException(status_code=403, detail="Not your post")
    await db.delete(post)
    await db.commit()


# ── Likes ──

@router.post("/{post_id}/like", status_code=200)
async def toggle_like(
    post_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    post = await db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    result = await db.execute(
        select(Like).where(Like.user_id == user.id, Like.post_id == post_id)
    )
    existing = result.scalars().first()

    if existing:
        await db.delete(existing)
        post.like_count = max(0, post.like_count - 1)
    else:
        db.add(Like(user_id=user.id, post_id=post_id))
        post.like_count += 1

    await db.commit()
    return {"liked": existing is None, "like_count": post.like_count}


# ── Comments ──

@router.post("/{post_id}/comments", response_model=CommentOut, status_code=201)
async def add_comment(
    post_id: int,
    payload: CommentCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    post = await db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comment = Comment(body=payload.body, author_id=user.id, post_id=post_id)
    db.add(comment)
    await db.commit()
    await db.refresh(comment)

    return CommentOut(
        id=comment.id,
        body=comment.body,
        author_id=comment.author_id,
        author_username=user.username,
        created_at=comment.created_at,
    )


@router.delete("/{post_id}/comments/{comment_id}", status_code=204)
async def delete_comment(
    post_id: int,
    comment_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(require_user),
):
    comment = await db.get(Comment, comment_id)
    if not comment or comment.post_id != post_id:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.author_id != user.id and not user.is_admin:
        raise HTTPException(status_code=403, detail="Not your comment")
    await db.delete(comment)
    await db.commit()
