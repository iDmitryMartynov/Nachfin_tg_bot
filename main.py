import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import BufferedInputFile, InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()

# Первая инлайн-клавиатура с кнопкой "Перейти в главное меню"
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Перейти в главное меню', callback_data="start_menu")]
    ]
)

# Вторая инлайн-клавиатура с 4 кнопками
main_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Законодательная база по выплатам военнослужащим", callback_data="button1")],
        [InlineKeyboardButton(text="Обнаружили переплату или недоплату?", callback_data="button2")],
        [InlineKeyboardButton(text="Список документов для получения выплат", callback_data="button3")],
        [InlineKeyboardButton(text="Расчет выплат за участие в СВО", callback_data="button4")],
        [InlineKeyboardButton(text="Консультация", callback_data="button5")],
    ]
)


@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    welcome_text = (
        "Добро пожаловать! Этот чат-бот создан с целью повышения финансовой грамотности военнослужащих. "
        "Здесь вы можете ознакомиться с действующим законодательством, касающимся денежного довольствия "
        "военнослужащих, а также о положенных выплатах."
    )
    with open('C:/Users/m4llb/OneDrive/Изображения/Saved Pictures/gerb.jpg', 'rb') as file:
        photo = BufferedInputFile(file.read(), filename='gerb.jpg')
        await message.answer_photo(
            photo=photo,
            caption=welcome_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=start_keyboard
            )
        
@dp.callback_query(lambda query: query.data == 'start_menu')
async def start_menu_callback(query: types.CallbackQuery):
    await query.message.answer(
        'Вы в главном меню. Выберете действие:',
        reply_markup=main_menu_keyboard
    )
    await query.answer()


@dp.callback_query(lambda query: query.data.startswith("button"))
async def main_menu_button_callback(query: types.CallbackQuery):
    await query.answer()


async def main():
    await dp.start_polling(bot)



asyncio.run(main())