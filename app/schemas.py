import datetime
from pydantic import BaseModel, ConfigDict


# ── Auth ──

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    display_name: str = ""


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ── Users ──

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: str
    display_name: str
    bio: str | None
    avatar_url: str | None
    is_admin: bool
    is_active: bool
    created_at: datetime.datetime


class UserUpdate(BaseModel):
    display_name: str | None = None
    bio: str | None = None
    avatar_url: str | None = None


class AdminUserUpdate(BaseModel):
    is_admin: bool | None = None
    is_active: bool | None = None


# ── Posts ──

class PostCreate(BaseModel):
    title: str
    body: str
    category: str = "discussion"
    link_url: str | None = None


class PostUpdate(BaseModel):
    title: str | None = None
    body: str | None = None
    link_url: str | None = None


class CommentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    body: str
    author_id: int
    author_username: str = ""
    created_at: datetime.datetime


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    body: str
    category: str = "discussion"
    link_url: str | None = None
    author_id: int
    author_username: str = ""
    author_display_name: str = ""
    author_avatar_url: str | None = None
    like_count: int
    liked_by_me: bool = False
    comment_count: int = 0
    comments: list[CommentOut] = []
    created_at: datetime.datetime
    updated_at: datetime.datetime


# ── Comments ──

class CommentCreate(BaseModel):
    body: str


# ── Admin Stats ──

class AdminStats(BaseModel):
    total_users: int
    total_posts: int
    total_comments: int
