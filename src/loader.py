from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
from middlewares.session import SessionMiddleware
import handlers

bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

storage = MemoryStorage()

dp = Dispatcher(bot=bot, storage=storage)

# Register middlewares
dp.message.middleware(SessionMiddleware())
dp.inline_query.middleware(SessionMiddleware())

# Register routers
dp.include_routers(
    handlers.admin_notify_router,
    handlers.command_router,
    handlers.voicy_router
)
