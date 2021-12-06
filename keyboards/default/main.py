from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📲 Kontakt ulashish',request_contact=True)
			

        ]
    ],
    resize_keyboard=True
)
joy=ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text='🕹 Lokatsiya yuborish', request_location=True)
			
        ]
    ],
    resize_keyboard=True
)





