import asyncio
from os import getenv

from aiogram import Bot, Dispatcher

from handlers import register_handlers


from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()

register_handlers(dp)

async def main():
    await dp.start_polling(bot)


asyncio.run(main())