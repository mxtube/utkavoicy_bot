from loguru import logger

from aiogram import Router, types

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.voicy import Voicy

voicy_router = Router(name='Voicy router')


@voicy_router.inline_query()
async def voicy_message(inline_query: types.InlineQuery, session: AsyncSession):
    logger.info(f"Inline query voice from user {inline_query.from_user.username}")
    query = await session.execute(select(Voicy))
    voices = query.scalars().all()
    menu = []
    for index, voice in enumerate(voices, start=1):
        menu.append(
            types.InlineQueryResultVoice(
                id=str(index),
                title=voice.name,
                voice_url=f'{voice.url}'
            )
        )
    await inline_query.answer(menu, cache_time=1, is_personal=True)
