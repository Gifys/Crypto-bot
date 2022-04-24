from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from main import bot, dp
from keybords import keyboard1, ton_key, ton_back, bnb_key, bnb_back, cb
from parser_crypto import course


# Монеты
global ton_course
global bnb_course


@dp.message_handler(commands='start')
async def menu(message: Message):
    await message.answer('Выбери криптовалюту за которой хочешь проследить:', reply_markup=keyboard1)

############# Ton #############
@dp.callback_query_handler(cb.filter(name="ton")) # text_contains='ton'
async def ton(call: CallbackQuery):
    global ton_course
    ton_course = course('toncoin')

    await call.message.edit_text(f"TON — это блокчейн третьего поколения, разработанный в 2018 году братьями "
                                 f"Дуровыми, основателями Telegram Messenger. Позже он был передан нашему "
                                 f"открытому сообществу TON, которое с тех пор поддерживает и развивает его.\n\n"
                                 f"<em><b>Курс TON: {ton_course}</b></em>")

    await call.message.edit_reply_markup(reply_markup=ton_key) # новая клавиатура вместо старой

@dp.callback_query_handler(text_contains='new_ton_course')
async def update_ton_course(call: CallbackQuery):
    global ton_course

    await call.message.edit_text(f"TON — это блокчейн третьего поколения, разработанный в 2018 году братьями "
                                 f"Дуровыми, основателями Telegram Messenger. Позже он был передан нашему "
                                 f"открытому сообществу TON, которое с тех пор поддерживает и развивает его.\n\n"
                                 
                                 f"<em><b>Курс TON: <strike>{ton_course}</strike> {course('toncoin')}</b></em>")

    await call.message.edit_reply_markup(reply_markup=ton_key)

    ton_course = course('toncoin')

@dp.callback_query_handler(text_contains="additional_ton_information")
async def ton_info(call: CallbackQuery):
    await call.message.edit_text('Тут инфа')

    await call.message.edit_reply_markup(reply_markup=ton_back)

@dp.callback_query_handler(text_contains="back_to_ton_menu")
async def back_ton_menu(call: CallbackQuery):
    global ton_course
    ton_course = course('toncoin')

    await call.message.edit_text(f"TON — это блокчейн третьего поколения, разработанный в 2018 году братьями "
                                 f"Дуровыми, основателями Telegram Messenger. Позже он был передан нашему "
                                 f"открытому сообществу TON, которое с тех пор поддерживает и развивает его.\n\n"
                                 f"<em><b>Курс TON: {ton_course}</b></em>")

    await call.message.edit_reply_markup(reply_markup=ton_key)

############# BNB #############
@dp.callback_query_handler(cb.filter(name="bnb")) # text_contains='bnb'
async def bnb(call: CallbackQuery):
    global bnb_course
    bnb_course = course('bnb')

    # photo = InputFile("files/test.png")
    # await bot.send_photo(chat_id=types.message.Chat.id, photo=photo)

    await call.message.edit_text(f"BNB — это криптовалюта, которая поддерживает экосистему Binance. BNB является "
                                 f"одним из самых популярных utility-токенов в мире. Вы можете не только покупать "
                                 f"или продавать BNB, как и любую другую криптовалюту, но и воспользоваться широким "
                                 f"спектром дополнительных преимуществ.\n\n"

                                 f"<em><b>Курс BNB: {bnb_course}</b></em>")

    await call.message.edit_reply_markup(reply_markup=bnb_key)

@dp.callback_query_handler(text_contains='new_bnb_course')
async def update_bnb_course(call: CallbackQuery):
    global bnb_course

    await call.message.edit_text(f"BNB — это криптовалюта, которая поддерживает экосистему Binance. BNB является "
                                 f"одним из самых популярных utility-токенов в мире. Вы можете не только покупать "
                                 f"или продавать BNB, как и любую другую криптовалюту, но и воспользоваться широким "
                                 f"спектром дополнительных преимуществ.\n\n"

                                 f"<em><b>Курс BNB: <strike>{bnb_course}</strike> {course('bnb')}</b></em>")

    await call.message.edit_reply_markup(reply_markup=bnb_key)

    bnb_course = course('bnb')

@dp.callback_query_handler(text_contains="additional_bnb_information")
async def bnb_info(call: CallbackQuery):
    await call.message.edit_text('Тут инфа про bnb')

    await call.message.edit_reply_markup(reply_markup=bnb_back)

@dp.callback_query_handler(text_contains="back_to_bnb_menu")
async def back_bnb_menu(call: CallbackQuery):
    global bnb_course
    bnb_course = course('bnb')

    await call.message.edit_text(f"BNB — это криптовалюта, которая поддерживает экосистему Binance. BNB является "
                                 f"одним из самых популярных utility-токенов в мире. Вы можете не только покупать "
                                 f"или продавать BNB, как и любую другую криптовалюту, но и воспользоваться широким "
                                 f"спектром дополнительных преимуществ.\n\n"

                                 f"<em><b>Курс BNB: {bnb_course}</b></em>")

    await call.message.edit_reply_markup(reply_markup=bnb_key)

############# Общий кусок #############
@dp.callback_query_handler(text_contains="backspase")
async def backspase(call: CallbackQuery):
    await call.message.edit_text('Выбери криптовалюту за которой хочешь проследить:')

    await call.message.edit_reply_markup(reply_markup=keyboard1)

@dp.callback_query_handler(text_contains='main_cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Отмена', show_alert=True) # Выводит сообщение об отмене

    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_text("Спасибо, что посетили")

''' Машина состояния '''
# @dp.message_handler(commands='tshop')
# async def starting(message: Message):
#     await message.answer(f"Hello, {message.from_user.first_name}", reply_markup=keyboard)
#
# @dp.message_handler(Text(equals=["TON", "BNB"]))
# async def choice(message: Message):
#     but = message.text
#
#     if but == "TON":
#         await message.answer("Ton is a beati", reply_markup=ReplyKeyboardRemove())
#     elif but == "BNB":
#         await message.answer("BNB is a beati", reply_markup=ReplyKeyboardRemove())

@dp.message_handler()
async def echo(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}, что я должен на это ответить?")