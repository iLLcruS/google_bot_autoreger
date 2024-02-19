import logging
import asyncio
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, Router, dispatcher, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from registration_module import registration_router

from registration_module.registration_router import router as registration_engine_router


from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Загрузка переменных окружения

bot_token = os.environ.get('BOT_TOKEN')

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Инициализация бота
bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
# Создание маршрутизатора
router = Router()


@router.message(F.text == '/start')
async def send_welcome(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(
        types.KeyboardButton(text="Auto-registration"),
    )
    await message.answer(text="<b>Choose action: </b>", reply_markup=builder.as_markup(resize_keyboard=True))



async def main():
    await dp.start_polling(bot, close_bot_session=True)
async def run():
    dp.include_router(router)
    dp.include_router(registration_engine_router)
    bot_task = asyncio.create_task(main())
    await asyncio.gather(bot_task)


if __name__ == "__main__":
    while True:
        asyncio.run(run())
