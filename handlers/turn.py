from create_bot import dp, bot
from aiogram.types import Message, InputFile
from text import rulesXO
from XOgame import get_game, set_game, set_mark, bot_pass
from keyboards import kb_turn, kb_game
from random import choice

@dp.message_handler(commands=['да'])
async def com_start(message: Message):
    photo = InputFile('images/krestiki-noliki.png')
    name = message.from_user.full_name
    chat_id = message.chat.id
    rules = rulesXO
    if get_game():
        await dp.bot.send_photo(chat_id=chat_id,
                                photo=photo,
                                caption=f'''{name}! ОЙ, а игра уже идет! Ход менять нельзя. 
                                Если хочешь начать с начала - пиши /start''',)
    else:
        await dp.bot.send_photo(chat_id=chat_id,
                                photo=photo,
                                caption=f'{name}! {rules}',
                                reply_markup=kb_turn)

@dp.message_handler(commands= ['орел', 'решка'])
async def orel_reshka(message: Message):
    if get_game():
        await message.answer(f'{message.from_user.first_name}! Аущ! А игра то уже идет! Если хочешь начать сначала пиши /start')
    coin_random = choice(['орел', 'решка'])
    set_game()
    await message.answer(f'Сейчас подброшу монетку! {coin_random.capitalize()}!')
    if coin_random == 'орел':
        photo = open('images/ozel.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    else:
        photo = open('pictures/pagonya.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    if message.text[1:] == coin_random:
        await bot.send_message( f'Эй, {message.from_user.first_name}! Ты ходишь первым', reply_markup=kb_game)
    else:
        set_mark()
        bot_pace()
        await bot.send_message(f'Не повезло тебе, {message.from_user.first_name}! Первым хожу я', reply_markup=kb_game)
