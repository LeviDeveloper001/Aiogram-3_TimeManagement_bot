from typing import Iterable

from aiogram import Router


class BaseRouter(Router):
    def set_middlewares_for_all_events(self, middlewares:Iterable):
        for mw in middlewares:
            self.message.middleware(mw)
            self.callback_query.middleware(mw)
            

