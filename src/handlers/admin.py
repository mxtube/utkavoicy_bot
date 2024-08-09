from loguru import logger
from config import settings
from aiogram import Router, Bot

admin_notify_router = Router(name='Admin Notification')


@admin_notify_router.startup()
async def on_startup_notify(bot: Bot):
    MESSAGE: str = 'Bot running'
    for admin in settings.ADMIN_IDS:
        try:
            logger.info(f'Send notifying to admin {admin}, message: {MESSAGE}')
            await bot.send_message(chat_id=admin, text=MESSAGE)
        except Exception as e:
            logger.warning(f'{e} {admin}')


@admin_notify_router.shutdown()
async def on_shutdown_notify(bot: Bot):
    MESSAGE: str = 'Bot shutdown'
    for admin in settings.ADMIN_IDS:
        try:
            logger.info(f'Send notifying to admin {admin}, message: {MESSAGE}')
            await bot.send_message(chat_id=admin, text=MESSAGE)
        except Exception as e:
            logger.warning(f'{e} {admin}')
