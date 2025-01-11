import asyncio

from src.dispatcher import dispatcher
from src.bot import bot

async def main():
    await dispatcher.start_polling(bot)



if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')

