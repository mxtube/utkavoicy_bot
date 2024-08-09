from loguru import logger

from aiogram import Router, types
from aiogram.filters import CommandStart


command_router = Router(name='bot_commands')


@command_router.message(CommandStart())
async def start(message: types.Message):
    logger.info(f'User {message.from_user.username} send command {message.text}')
    answer_message = f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nПолучается это бот 🦆'
    await message.answer(answer_message)
    logger.info(f'Bot send to user message: {answer_message}')
