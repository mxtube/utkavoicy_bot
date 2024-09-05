from loguru import logger
from aiogram import types
from typing import Optional

from config import settings
from loader import bot


class BotSettings:

    def __init__(self, current_settings):
        self.bot_name: Optional[str] = settings.BOT_NAME
        self.bot_short_desc: Optional[str] = settings.BOT_SHORT_DESCRIPTION
        self.bot_desc: Optional[str] = settings.BOT_DESCRIPTION
        self.current_setting = current_settings

    async def setting_bot_menu(self):
        logger.info('Start setting bot menu')
        await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
        logger.info('Delete all commands from bot menu')
        private = [
            types.BotCommand(command='start', description='Запустить/Перезапустить бота'),
            types.BotCommand(command='help', description='Как использовать бота'),
            types.BotCommand(command='bug', description='Как сообщить об ошибке (Только в приватном чате)')
        ]
        await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
        logger.info(f'Finish configuring bot menu. Count command ({private.__len__()})')

    async def is_bot_name_valid(self) -> bool:
        logger.info('Checking valid bot name')
        return True if self.current_setting.first_name == self.bot_name and self.bot_name is not None else False

    async def change_bot_name(self):
        try:
            if not await self.is_bot_name_valid():
                logger.info(f'Change bot name, from: {self.bot_name} to {settings.BOT_NAME}')
                await bot.set_my_name(settings.BOT_NAME)
                logger.info('Bot name changed')
            logger.info('Bot name is valid')
        except Exception as e:
            logger.error(f'Change bot name error, {e}')

    async def initial_settings(self):
        logger.info('Configure bot')
        await self.change_bot_name()
        await self.setting_bot_menu()
