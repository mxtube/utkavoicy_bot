from loguru import logger

from typing import ContextManager
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from config import settings

sa_async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=settings.DEBUG
)

sa_session_factory = async_sessionmaker(
    bind=sa_async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()


async def initialize_database():
    logger.info('Database initialization started')
    async with sa_async_engine.begin() as conn:

        await conn.run_sync(Base.metadata.drop_all)
        logger.info('All tables dropped')

        await conn.run_sync(Base.metadata.create_all)
        logger.info(f'Tables created: {len(Base.metadata.tables)}')

        for table_name in Base.metadata.tables:
            logger.info(f'Table {table_name} created')

        logger.info('Database initialization completed')


@asynccontextmanager
async def get_async_sa_connection():
    async with sa_async_engine.connect() as connection:
        yield connection


@asynccontextmanager
async def get_async_sa_session() -> ContextManager[AsyncSession]:
    async with sa_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
