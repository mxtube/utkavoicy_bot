from loguru import logger

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .sa import intpk, created_at, updated_at, deleted_at, Base


class User(Base):

    __tablename__ = 'user'

    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    deleted_at: Mapped[deleted_at]

    repr_cols_num = 6
    repr_cols = ('created_at', )

    @staticmethod
    async def create_or_update(session: AsyncSession, user_data: dict):
        result = await session.execute(select(User).filter_by(tg_id=user_data['id']))
        user = result.scalars().first()

        if user:
            user.username = user_data['username']
            user.first_name = user_data['first_name']
            user.last_name = user_data['last_name']
            await session.commit()
            logger.info(f'User {user.username} was updated in the database')
        else:
            new_user = User(
                username=user_data['username'],
                tg_id=user_data['id'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            session.add(new_user)
            await session.commit()
            logger.info(f'User {new_user.username} add in the database')

    @classmethod
    async def is_user_exists(cls, session: AsyncSession, tg_id: int) -> bool:
        logger.info(f'Check user id {tg_id} in database')
        result = await session.execute(select(cls).where(cls.tg_id == tg_id))
        user = result.fetchone()
        return bool(user)
