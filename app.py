import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import BufferedInputFile, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


API_TOKEN = "7576807512:AAF_sb_1Ju2bqrDgyBtOPBx6p_V9kc_hAnQ"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


main_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Перейти в главное меню', callback_data="main_menu")]
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
            reply_markup=main_menu_keyboard
            )
        
@dp.callback_query(lambda query: query.data == 'main_menu')
async def main_menu_callback(query: types.CallbackQuery):
    await query.message.answer("Вы перешли в главное меню.")
    await query.answer()

async def main():
    await dp.start_polling(bot)



asyncio.run(main())