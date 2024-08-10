from loguru import logger

from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User

from aiogram import Router, types
from aiogram.filters import CommandStart, Command


command_router = Router(name='Bot commands')


@command_router.message(CommandStart())
async def start(message: types.Message, session: AsyncSession):
    logger.info(f'User {message.from_user.username} send command {message.text}')
    answer_message = f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nПолучается это бот 🦆'
    await User.create_or_update(session, message.from_user.__dict__)
    await message.answer(answer_message)
    logger.info(f'Bot send to user message: {answer_message}')


@command_router.message(Command('help'))
async def help_cmd(message: types.Message):
    logger.info(f'User {message.from_user.username} send command {message.text}')
    answer_message = ('Для использования бота, необходимо упомянуть его @ в нужной беседе и выбрать '
                      'необходимое сообщение.')
    await message.answer(answer_message)
    logger.info(f'Bot send to user message: {answer_message}')
