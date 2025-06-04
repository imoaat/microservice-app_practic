import asyncio
import logging
from bot.dispatcher import bot, dp
from bot.handlers import router

async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
