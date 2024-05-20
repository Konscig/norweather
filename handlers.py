import asyncio
import datetime
import time

from aiogram import types

from keyboards import main_menu, exitor_menu
from main import baltasar, dp
from newinfo import aktirovka

current_date = str(datetime.datetime.now())


@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message):
    await message.answer(text="⚡️Привет, я NORWEATHERBOT!")
    await baltasar.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    time.sleep(1)
    await message.answer(text=f"Могу сообщить тебе:\
        <b>\n•погоду\n•актировку\n•состояние автодороги в Норильске.</b>\n\n<i>Для этого пропиши команду /weather"
                              f"\n(или просто нажми на кнопку).</i>", reply_markup=main_menu)


@dp.message_handler(commands=['weather'], state="*")
async def start(message: types.Message):
    user_name = message.from_user.full_name
    msg = await message.answer(text=aktirovka(user_name))
    await baltasar.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await asyncio.sleep(10)


@dp.callback_query_handler(text="k1")
async def dataterr(callback: types.CallbackQuery):
    user_name = callback.from_user.first_name
    await callback.message.answer(text=aktirovka(user_name), reply_markup=exitor_menu)
    await callback.message.delete_reply_markup()


@dp.callback_query_handler(text="k3")
async def dataterr(callback: types.CallbackQuery):
    await callback.message.answer(text="Чем я могу вам помочь?", reply_markup=main_menu)
    await callback.message.delete_reply_markup()


@dp.message_handler(content_types=types.ContentType.TEXT)
async def eho_callers1(message: types.Message):
    msg = await message.answer(text="Чем я могу вам помочь?", reply_markup=main_menu)
    await baltasar.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await asyncio.sleep(10)
    await msg.delete()
