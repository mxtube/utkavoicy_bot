from aiogram import BaseMiddleware, types

from typing import Callable, Awaitable, Any

from database.core import get_async_sa_session


class SessionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: types.TelegramObject,
        data: dict[str, Any]
    ) -> Any:
        async with get_async_sa_session() as session:
            data['session'] = session
            return await handler(event, data)
