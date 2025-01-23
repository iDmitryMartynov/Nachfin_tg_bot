from aiogram import Dispatcher
from aiogram.filters import Command
from .start import start_cmd
from .main_menu import start_menu_callback, command_menu
from .button1 import button1_callback

def register_handlers(dp: Dispatcher):
    dp.message.register(start_cmd, Command('start'))
    dp.message.register(command_menu, Command('menu'))
    dp.callback_query.register(start_menu_callback, lambda query: query.data == 'start_menu')
    dp.callback_query.register(button1_callback, lambda query: query.data == "button1")
