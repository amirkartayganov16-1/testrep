from aiogram import executor
from config import dp
import logging
from handlers import callback, client, notification, fsmadminmenu
from database import botttt

async def on_start_up(_):
    botttt.sql_create()

client.register_hendlers_client(dp)
callback.register_hendlers_callback(dp)
fsmadminmenu.register_hendler_fsmAdminGetUser(dp)

notification.register_hendlers_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, on_startup=on_start_up)