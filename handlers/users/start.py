from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main import menuStart
from loader import dp
from keyboards.default.main import joy
from aiogram.types import ContentType


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuStart)

@dp.message_handler(content_types=ContentType.CONTACT,is_sender_contact=True)
async def location(message:types.Message):
    await message.answer(f"Juda soz {message.from_user.full_name} endi lokatsiyangizni yuboring!",reply_markup=joy)
    











