from aiogram import Bot, executor, Dispatcher, types

TOKEN = '5169813611:AAFhsFdSJKFEjpAUEcw9HJocAZwPC559rsE'
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

if __name__ = '__main__':
    executor.start_polling(dp, skip_updates=False)
