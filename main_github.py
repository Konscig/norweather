from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


BOT_TOKEN = "YOURTOKEN"
baltasar = Bot(BOT_TOKEN, parse_mode="HTML")

dp = Dispatcher(baltasar, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

if __name__ == "__main__":
    try:
        from handlers import dp

        executor.start_polling(dp)
    except Exception as error:
        print("Произошла ошибка,", error)
