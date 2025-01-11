import datetime as dt

from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from .base_router import BaseRouter
from src.db.manager import Manager, ConditionEqualsValues

class ManagementRouter(BaseRouter):
    def __init__(self, *, name = None):
        super().__init__(name=name)
        self.set_handlers()
        
    def set_handlers(self):
        
        @self.message(Command('begin'))
        async def cmd_do(message:Message):
            await message.answer('command /begin')
            
        @self.message(Command('stop'))
        async def cmd_stop(message:Message):
            await message.answer('command /stop')
            
    



