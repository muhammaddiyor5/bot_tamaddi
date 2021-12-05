from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main import menuStart
from loader import dp
from keyboards.default.main import location



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuStart)

@dp.mesaage_handler(text_contains='Salom')
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=location)











