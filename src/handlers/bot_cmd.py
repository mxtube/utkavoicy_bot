from loguru import logger

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import User

from aiogram import Router, types
from aiogram.filters import CommandStart, Command


command_router = Router(name='Bot commands')


@command_router.message(CommandStart())
async def start(message: types.Message, session: AsyncSession):
    logger.info(f'User {message.from_user.username} send command {message.text}')
    answer_message = f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nПолучается это бот 🦆'

    result = await session.execute(select(User).filter_by(tg_id=message.from_user.id))
    user = result.scalars().first()

    if user:
        user.username = message.from_user.username
        user.first_name = message.from_user.first_name
        user.last_name = message.from_user.last_name
        await session.commit()
        logger.info(f'User {user.username} was updated in the database')
    else:
        new_user = User(
            username=message.from_user.username,
            tg_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name
        )
        session.add(new_user)
        await session.commit()
        logger.info(f'User {new_user.username} add in the database')

    await message.answer(answer_message)
    logger.info(f'Bot send to user message: {answer_message}')


@command_router.message(Command('help'))
async def help_cmd(message: types.Message):
    logger.info(f'User {message.from_user.username} send command {message.text}')
    answer_message = ('Для использования бота, необходимо упомянуть его @ в нужной беседе и выбрать '
                      'необходимое сообщение.')
    await message.answer(answer_message)
    logger.info(f'Bot send to user message: {answer_message}')
