from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
import handlers

bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

storage = MemoryStorage()

dp = Dispatcher(bot=bot, storage=storage)

# Register routers
dp.include_routers(
    handlers.command_router,
    handlers.admin_notify_router
)
