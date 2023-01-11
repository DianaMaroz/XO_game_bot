from create_bot import dp
from aiogram.types import CallbackQuery, InputMediaPhoto
from XOgame import get_mark, field, bot_pace, check_win, check_draw

from keyboards import create_game_menu, stroke, kb_back



@dp.callback_query_handler(stroke.filter(mark='user_stroke'))
async def game_pace(call: CallbackQuery):
    print('ход игрока')
    current_chat_id = call.message.chat.id
    current_message_id = call.message.message_id
    mark_pace = get_mark()
    cell = int(call.data.split(':')[-1])
    print(cell)
    if field[cell] in ['X', 'O']:
        photo = open('images/game.png', 'rb')
        await dp.bot.edit_message_media(
            media=InputMediaPhoto(media=photo, caption="Это поле уже занято!"),
            chat_id=current_chat_id, message_id=current_message_id,
            reply_markup=create_game_menu())
    else:
        field[cell] = mark_pace
        print(field)
        if check_draw():
            photo = open('images/game.png', 'rb')
            await dp.bot.edit_message_media(
                media=InputMediaPhoto(media=photo, caption="Ничья!"),
                chat_id=current_chat_id, message_id=current_message_id,
                reply_markup=kb_back)
        else:
            if check_win():
                photo = open('images/win.png', 'rb')
                await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo, caption="Вы выиграли!"),
                                                chat_id=current_chat_id, message_id=current_message_id,
                                                reply_markup=kb_back)
            else:
                print('ход бота')
                bot_pace(field)
                print(field)
                if check_win():
                    photo = open('images/loose.jpg', 'rb')
                    await dp.bot.edit_message_media(
                        media=InputMediaPhoto(media=photo, caption="Вы проиграли"),
                        chat_id=current_chat_id, message_id=current_message_id,
                        reply_markup=kb_back)
                else:
                    photo = open('images/game.png', 'rb')
                    await dp.bot.edit_message_media(
                        media=InputMediaPhoto(media=photo, caption="Я походил, теперь ваш черед"),
                        chat_id=current_chat_id, message_id=current_message_id,
                        reply_markup=create_game_menu())



