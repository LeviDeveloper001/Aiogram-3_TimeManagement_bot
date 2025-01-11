from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

class PrivateChatTypeFilter(BaseFilter):
    async def __call__(self, message:Union[Message, CallbackQuery], *args, **kwds):
        if message.chat.type not in ('private', ): return
        return await super().__call__(*args, **kwds)
