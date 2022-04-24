from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import URL_TON, URL_BNB, \
    URL_BUY_TON_FROM_FTX, URL_BUT_BNB_FROM_BINANCE


cb = CallbackData('buy', 'id', 'name', 'exchange_rate') # Это я вообще не использую, и пока хз как убрать, что

############# Main inline #############
keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="TON", callback_data='buy:0:ton:USDT'),
            InlineKeyboardButton(text="BNB", callback_data='buy:1:bnb:USDT')
        ],
        [
            InlineKeyboardButton(text="Cancel", callback_data='main_cancel')
        ]
    ]
)

############# Inline for TON #############
ton_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Где купить ?', url=URL_BUY_TON_FROM_FTX),
            InlineKeyboardButton(text="Обновить курс", callback_data="new_ton_course")
        ],
        [
            InlineKeyboardButton(text="Официальный сайт", url=URL_TON),
            InlineKeyboardButton(text="Подробнее о монете", callback_data="additional_ton_information")

        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="backspase") # общая кнопка для выхода в главное меню
        ]
    ]
)

ton_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Выбрать другую монету", callback_data="backspase"), # общая кнопка для выхода в главное меню
            InlineKeyboardButton(text="Назад", callback_data="back_to_ton_menu")
        ]
    ]
)

############# Inline for BNB #############
bnb_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Где купить ?', url=URL_BUT_BNB_FROM_BINANCE),
            InlineKeyboardButton(text="Обновить курс", callback_data="new_bnb_course")
        ],
        [
            InlineKeyboardButton(text="Официальный сайт", url=URL_BNB),
            InlineKeyboardButton(text="Подробнее о монете", callback_data="additional_bnb_information")

        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="backspase") # общая кнопка для выхода в главное меню
        ]
    ]
)

bnb_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Выбрать другую монету", callback_data="backspase"), # общая кнопка для выхода в главное меню
            InlineKeyboardButton(text="Назад", callback_data="back_to_bnb_menu")
        ]
    ]
)
