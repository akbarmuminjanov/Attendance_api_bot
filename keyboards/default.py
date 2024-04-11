from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="📗 информация"),
            KeyboardButton(text="📃 сообщения"),
        ]
    ],
    resize_keyboard=True
)

