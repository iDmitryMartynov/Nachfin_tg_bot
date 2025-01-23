from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# "Перейти в главное меню"
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Перейти в главное меню', callback_data="start_menu")]
    ]
)

# Главное меню
main_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Законодательная база по выплатам военнослужащим", callback_data="button1")],
        [InlineKeyboardButton(text="Обнаружили переплату или недоплату?", callback_data="button2")],
        [InlineKeyboardButton(text="Список документов для получения выплат", callback_data="button3")],
        [InlineKeyboardButton(text="Расчет выплат за участие в СВО", callback_data="button4")],
        [InlineKeyboardButton(text="Консультация", callback_data="button5")],
    ]
)

# Законодательная база по выплатам военнослужащим
button1_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ЕНВЛ", callback_data="ENVL")],
        [InlineKeyboardButton(text="ЕНКК", callback_data="button2")],
        [InlineKeyboardButton(text="ЕНГТ", callback_data="button3")],
        [InlineKeyboardButton(text="НОУС", callback_data="button4")],
        [InlineKeyboardButton(text="ЕНОД", callback_data="button5")],
    ]
)
