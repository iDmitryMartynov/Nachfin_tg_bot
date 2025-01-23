from aiogram import types

from keyboards.main_menu import button1_keyboard


async def button1_callback(query: types.CallbackQuery):
    await query.message.answer(
        'Выберете название выплаты',
        reply_markup=button1_keyboard
    )

