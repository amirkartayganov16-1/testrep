from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Bot, Dispatcher, executor
import logging
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

ADMIN = 1044771018

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Салам хозяин {message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
async def problem1(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1"
    )
    murkup.add(button_call_1)

    question = 'Какая страна производит больше всего кофе в мире?'
    answers = 'Колумбия Индонезия Бразилия Вьетнам'.split()
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        reply_markup=murkup
                        )
 
@dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def problem2(call: types.CallbackQuery):
    murkup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_2"
    )
    murkup.add(button_call_2)

    question = "Какой герой мультфильма живет в ананасе под водой?"
    answers = "Камбала Немо Рик ГубкаБоб".split()
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3,
                        reply_markup = murkup
                        )

@dp.callback_query_handler(lambda func: func.data == "button_call_2")
async def problem3(call: types.CallbackQuery):
    question = "В какой стране находится Прага?"
    answers = "Испания Бразилия Чехия Англия".split()
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2
                        )

@dp.message_handler(content_types=["text"])
async def echo_message(message: types.message):
    if not message.reply_to_message:
        await message.reply("Команда должна быть ответом на сообщение!")
    else:
        if message.text.startswith('pin'):
            await bot.pin_chat_message(message.chat.id, message.message_id)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)