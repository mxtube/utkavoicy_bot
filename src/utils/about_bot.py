from loguru import logger
from aiogram import types

from loader import bot


async def setting_bot_menu():
    logger.info('Start configure bot menu')
    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    logger.info('Delete all commands from bot menu')
    private = [
        types.BotCommand(command='start', description='Запустить/Перезапустить бота'),
        types.BotCommand(command='help', description='Как использовать бота')
    ]
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    logger.info(f'Finish configuring bot menu. Count command ({private.__len__()})')
