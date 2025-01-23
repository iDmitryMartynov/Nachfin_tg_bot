from aiogram import types
from aiogram.types import BufferedInputFile
from aiogram.enums import ParseMode

from keyboards.main_menu import start_keyboard



async def start_cmd(message: types.Message):
    welcome_text = (
        'Добро пожаловать! Этот чат-бот создан с целью повышения финансовой грамотности военнослужащих.'
        'Здесь вы можете ознакомиться с действующим законодательством, касающимся денежного довольствия'
        'военнослужащих, а также о положенных выплатах.'
    )
    with open('assets/gerb.jpg', 'rb') as file:
        photo = BufferedInputFile(file.read(), filename='gerb.jpg')
        await message.answer_photo(
            photo=photo,
            caption=welcome_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=start_keyboard
            )