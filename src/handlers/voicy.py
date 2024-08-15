from loguru import logger

from aiogram import Router, types

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User, Voicy, AnalyticsVoicy

voicy_router = Router(name='Voicy router')


@voicy_router.inline_query()
async def voicy_message(inline_query: types.InlineQuery, session: AsyncSession):
    logger.info(f"Inline query voice from user {inline_query.from_user.username}")
    user = await User.is_user_exists(session, inline_query.from_user.id)
    if user:
        query = await session.execute(select(Voicy).where(Voicy.deleted_at.is_(None)))
        voices = query.scalars().all()
        menu = []
        for index, voice in enumerate(voices, start=1):
            menu.append(
                types.InlineQueryResultVoice(
                    id=str(index),
                    title=voice.get_name(),
                    voice_url=f'{voice.url}'
                )
            )
        await inline_query.answer(menu, cache_time=1, is_personal=True)
    menu = [types.InlineQueryResultVoice(id='1', title='Use /start in bot', voice_url='https://t.me/')]
    await inline_query.answer(results=menu, cache_time=1, is_personal=True)


@voicy_router.chosen_inline_result()
async def chosen_inline_result_handler(chosen_result: types.ChosenInlineResult, session: AsyncSession):
    result_id: int = int(chosen_result.result_id)
    user_id: int = int(chosen_result.from_user.id)

    logger.info(f'User {user_id} voice selected {result_id}')
    check_user = await session.execute(select(User).where(User.tg_id == user_id))
    user = check_user.scalars().first()

    av = AnalyticsVoicy(user_id=user.id, voicy_id=result_id)
    session.add(av)
    await session.commit()
    logger.info(f'Add voicy analytics {result_id}')
