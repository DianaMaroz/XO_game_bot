from create_bot import dp
from aiogram.types import Message, InputFile, CallbackQuery, InputMediaPhoto
from keyboards import kb_menu, stroke
from XOgame import set_game, get_game, new_field, field


@dp.callback_query_handler(stroke.filter(mark='back'))
async def com_start(call: CallbackQuery):
    if get_game():
        set_game()
    print(field)
    new_field()
    print(field)
    photo = InputFile('images/krestiki-noliki.jpg')
    name = call.message.chat.full_name
    chat_id = call.message.chat.id
    await dp.bot.send_photo(chat_id=chat_id,
                            photo=photo,
                            caption=f'{name}, добро пожаловать! Сыграем в крестики-нолики?',
                            reply_markup=kb_menu)


@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    photo = InputFile('images/krestiki-noliki.jpg')
    name = message.from_user.full_name
    chat_id = message.chat.id
    if get_game():
        set_game()

    await dp.bot.send_photo(chat_id=chat_id,
                            photo=photo,
                            caption=f'{name}, добро пожаловать! Сыграем в крестики-нолики?',
                            reply_markup=kb_menu)

@dp.message_handler(commands=['нет'])
async def com_start(message: Message):
    photo = InputFile('images/krestiki-noliki.jpg')
    name = message.from_user.full_name
    chat_id = message.chat.id
    await dp.bot.send_photo(chat_id=chat_id,
                            photo=photo,
                            caption=f'{name}, пока! Захочешь сыграть пиши /start')