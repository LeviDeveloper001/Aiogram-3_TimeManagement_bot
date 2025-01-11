from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from src.filters.main_filters import PrivateChatTypeFilter
from src.middlewares.main_middlewares import PrivateChatTypeMiddleware
from src.db.manager import Manager as DbManager

from .base_router import BaseRouter
from .management_router import ManagementRouter

class MainRouter(BaseRouter):
    including_routers = (
        ManagementRouter(),
    )
    including_middlewares = (
        PrivateChatTypeMiddleware(),
    )
    db_manager = DbManager()
    
    start_message = 'Start Message'
    def __init__(self, *, name = None):
        super().__init__(name=name)
        self.include_routers(*self.including_routers)
        self.set_middlewares_for_all_events(self.including_middlewares)
        self.set_handlers()
    
    def set_handlers(self):
        @self.message(CommandStart())
        async def cmd_start(message:Message):
            await message.answer(self.start_message)
            





    

