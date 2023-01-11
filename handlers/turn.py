from create_bot import dp, bot
from aiogram.types import Message, InputFile
from text import rulesXO
from XOgame import get_game, set_game, set_mark, bot_pace, field, get_mark, new_field
from keyboards import kb_turn, create_game_menu
from random import choice

@dp.message_handler(commands=['да'])
async def com_start(message: Message):
    photo = InputFile('images/krestiki-noliki.jpg')
    name = message.from_user.full_name
    chat_id = message.chat.id
    rules = rulesXO
    if get_game():
        await dp.bot.send_photo(chat_id=chat_id,
                                photo=photo,
                                caption=f'''{name}! ОЙ, а игра уже идет! Ход менять нельзя. 
                                Если хочешь начать с начала - пиши /start''',)
    else:
        print(field)
        new_field()
        print(field)
        await dp.bot.send_photo(chat_id=chat_id,
                                photo=photo,
                                caption=f'{name}! {rules}',
                                reply_markup=kb_turn)

@dp.message_handler(commands= ['орел', 'решка'])
async def orel_reshka(message: Message):
    name = message.from_user.first_name
    cur_chat_id = message.chat.id
    if get_game():
        await message.answer(f'{name}! Аущ! А игра то уже идет! Если хочешь начать сначала пиши /start')
    else:
        coin_random = choice(['орел', 'решка'])
        set_game()
        await message.answer(f'Сейчас подброшу монетку! {coin_random.capitalize()}!')
        if coin_random == 'орел':
            photo = open('images/ozel.jpg', 'rb')
            await bot.send_photo(chat_id=message.chat.id, photo=photo)
        else:
            photo = open('images/pagonya.jpg', 'rb')
            await bot.send_photo(chat_id=message.chat.id, photo=photo)
        if message.text[1:] == coin_random:
            if get_game() == 'O':
                set_mark()
            photo = open('images/start.jpg', 'rb')
            await dp.bot.send_photo(photo=photo, caption=f'Эй, {name}! Ты ходишь первым',
                                    chat_id=cur_chat_id, reply_markup=create_game_menu())
        else:
            if get_mark() == 'X':
                set_mark()
            bot_pace(field)
            photo = open('images/start.jpg', 'rb')
            await dp.bot.send_photo(photo=photo, caption=f'Не повезло тебе, {name}! Первый ход мой',
                                    chat_id=cur_chat_id, reply_markup=create_game_menu())