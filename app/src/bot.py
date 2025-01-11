from aiogram import Bot

from .settings import settings

class MainBot(Bot):
    pass


bot = MainBot(settings.token)


