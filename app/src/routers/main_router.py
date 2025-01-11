from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

class MainRouter(Router):
    start_message = 'Start Message'
    def __init__(self, *, name = None):
        super().__init__(name=name)
        @self.message(CommandStart())
        async def cmd_start(message:Message):
            await message.answer(self.start_message)
            





    

