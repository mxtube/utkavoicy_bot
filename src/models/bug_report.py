from loguru import logger

from .sa import intpk, created_at, updated_at, deleted_at, Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .user import User


class BugReport(Base):

    __tablename__ = 'bug_report'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    description: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    deleted_at: Mapped[deleted_at]

    repr_cols_num = 3

    @staticmethod
    async def create(session: AsyncSession, user_tg_id: int, text: str):
        result = await session.execute(select(User).filter_by(tg_id=user_tg_id))
        user = result.scalars().first()

        new_bug = BugReport(
            user_id=user.id,
            description=text
        )
        session.add(new_bug)
        await session.commit()
        logger.info(f'Save new bug {new_bug} in database')
