from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📲 Kontakt ulashish',request_contact=True)
			

        ]
    ]
)
location=ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text='🕹 Lokatsiya yuborish', request_location=True)
			

        ]
    ]
)




