from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="📗 malumot"),
            KeyboardButton(text="📃 xabarlar"),
        ]
    ],
    resize_keyboard=True
)

