import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from database.models import Base
# DB_LITE=sqlite+aiosqlite:///my_base.db
# engine = create_async_engine(os.getenv("DB_LITE"), echo=True)
# DB_URL=postgresql+asyncpg://login:password@localhost:5432/db_name
engine = create_async_engine(os.getenv("DB_LITE"), echo=True)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
