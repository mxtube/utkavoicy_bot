from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
from handlers import command_router

bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

storage = MemoryStorage()

dp = Dispatcher(bot=bot, storage=storage)

# Register routers
dp.include_routers(
    command_router,
)
