import asyncio
from loguru import logger

from loader import dp, bot
from utils import BotSettings
from database import initialize_database, initialize_voices
from utils.s3_client import S3Client

ALLOWED_UPDATES = ['message, edited message']


async def main():
    await initialize_database()
    voices = await S3Client().get_files()
    await initialize_voices(voices)
    await bot.delete_webhook(drop_pending_updates=True)
    await BotSettings(current_settings=await bot.get_me()).initial_settings()
    logger.info('Bot run')
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    logger.info('Bot stopped')


if __name__ == '__main__':
    logger.info('Application running')
    asyncio.run(main())
