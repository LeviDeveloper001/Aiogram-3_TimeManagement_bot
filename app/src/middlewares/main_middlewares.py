from typing import Callable, Union, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.types import TelegramObject


class PrivateChatTypeMiddleware(BaseMiddleware):
    allowed_event_types = (Message, CallbackQuery)
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ):
        if not isinstance(event, self.allowed_event_types):
            return False
        if (event.chat.type not in ('private', )):
            return False
        return await handler(event, data)
