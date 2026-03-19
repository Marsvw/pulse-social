from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.database import engine, Base
from app.routes_auth import router as auth_router
from app.routes_posts import router as posts_router
from app.routes_users import router as users_router
from app.routes_admin import router as admin_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    from sqlalchemy import text
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # Migrate: add new columns if they don't exist (safe to run repeatedly)
        for col, coltype, default in [
            ("category", "VARCHAR(20)", "'discussion'"),
            ("link_url", "VARCHAR(1000)", "NULL"),
        ]:
            try:
                await conn.execute(text(
                    f"ALTER TABLE posts ADD COLUMN {col} {coltype} DEFAULT {default}"
                ))
            except Exception:
                pass  # column already exists
    yield


app = FastAPI(title="SocialBlog", version="1.0.0", lifespan=lifespan)

app.include_router(auth_router)
app.include_router(posts_router)
app.include_router(users_router)
app.include_router(admin_router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/index.html")
