from loguru import logger

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .sa import intpk, deleted_at, created_at, Base


class Voicy(Base):

    __tablename__ = 'voicy'

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    url: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[created_at]
    deleted_at: Mapped[deleted_at]

    repr_cols_num = 4

    @staticmethod
    async def create_or_update(session: AsyncSession, voice_data: dict):
        result = await session.execute(select(Voicy).filter_by(name=voice_data['name']))
        voice = result.scalars().first()

        if voice:
            voice.name = voice_data['name']
            voice.url = voice_data['url']
            voice.deleted_at = None
            await session.commit()
            logger.info(f'Voice {voice.name} was updated in the database')
        else:
            new_voice = Voicy(name=voice_data['name'], url=voice_data['url'])
            session.add(new_voice)
            await session.commit()
            logger.info(f'Voice {new_voice.name} add in the database')
