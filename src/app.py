import asyncio
from loguru import logger

from loader import dp, bot
from utils import setting_bot_menu
from database import initialize_database
from database.voice_downloader import initialize_voice

ALLOWED_UPDATES = ['message, edited message']


async def main():
    await initialize_database()
    await initialize_voice()
    await bot.delete_webhook(drop_pending_updates=True)
    await setting_bot_menu()
    logger.info('Bot run')
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    logger.info('Bot stopped')


if __name__ == '__main__':
    logger.info('Application running')
    asyncio.run(main())
