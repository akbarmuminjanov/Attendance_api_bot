"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from get_student import get_student_info
from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboards.default import menu
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '7000372863:AAHaZjQF7IN8XanN5PGjc5HhODfRNmLMQ_w'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class User_id(StatesGroup):
    tg_id = State()

class Messages(StatesGroup):
    tg_id = State()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.answer(f"Добро пожаловать в Attendance bot", reply_markup=menu)


@dp.message_handler(Text(startswith='📗'))
async def send_welcome(message: types.Message):

    await message.answer("введите id ребенка")

    await User_id.tg_id.set()

@dp.message_handler(state=User_id.tg_id)
async def state_handler(message: types.Message, state: FSMContext):

    id_str = message.text

    id = int(id_str)
    
    print(type(id))
    print(id)

    info = get_student_info(id)

    text =f"ID: {info['tg_id']}\n"
    text +=f"name: {info['full_name']}\n"
    text +=f"group: {info['group']['name']}\n"

    await message.answer(f"{text}", reply_markup=menu)
    
    await state.finish()


@dp.message_handler(Text(startswith='📃'))
async def send_welcome(message: types.Message):

    await message.answer("введите id ребенка")

    await Messages.tg_id.set()

@dp.message_handler(state=Messages.tg_id)
async def state_handler(message: types.Message, state: FSMContext):

    id_str = message.text

    id = int(id_str)
    
    print(type(id))
    print(id)

    info = get_student_info(id)

    tex = "Сообщения\n"
    for i in info['marks']:
        checks = "✅" if i["checks"] else "❌"
        date = i["attendance"]['created']
        tex+=f"дата: {date} {checks}\n"

    for i in info['messages']:
        tex += f"Сообщение от наставника:  {i['body']}\n"
        

    await message.answer(f"{tex}", reply_markup=menu)
    
    await state.finish()


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)