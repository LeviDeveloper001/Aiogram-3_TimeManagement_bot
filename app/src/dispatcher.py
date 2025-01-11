from aiogram import Dispatcher
from .routers import MainRouter
from aiogram.fsm.strategy import FSMStrategy

class MainDispatcher(Dispatcher):
    def __init__(self, *, storage = None, fsm_strategy = FSMStrategy.USER_IN_CHAT, events_isolation = None, disable_fsm = False, name = None, **kwargs):
        super().__init__(storage=storage, fsm_strategy=fsm_strategy, events_isolation=events_isolation, disable_fsm=disable_fsm, name=name, **kwargs)
        self.include_routers(MainRouter())



dispatcher = MainDispatcher()

