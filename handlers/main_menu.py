from aiogram import types

from keyboards.main_menu import main_menu_keyboard, button1_keyboard 


async def start_menu_callback(query: types.CallbackQuery):
    await query.message.answer(
        'Вы в главном меню. Выберете действие:',
        reply_markup=main_menu_keyboard
    )
    await query.answer()


async def command_menu(message: types.Message):
    await message.answer(
        'Вы в главном меню',
        reply_markup=main_menu_keyboard
    )

