from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.database import engine, Base
from app.routes_auth import router as auth_router
from app.routes_accounts import router as accounts_router
from app.routes_transactions import router as transactions_router
from app.routes_upload import router as upload_router
from app.routes_analytics import router as analytics_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    from sqlalchemy import text
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # Migrations for existing DB
    migrations = [
        "ALTER TABLE users ADD COLUMN IF NOT EXISTS currency VARCHAR(3) DEFAULT 'USD'",
    ]
    for sql in migrations:
        try:
            async with engine.begin() as conn:
                await conn.execute(text(sql))
        except Exception:
            pass
    yield


app = FastAPI(title="Pulse Finance", version="2.0.0", lifespan=lifespan)

app.include_router(auth_router)
app.include_router(accounts_router)
app.include_router(transactions_router)
app.include_router(upload_router)
app.include_router(analytics_router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/index.html")
