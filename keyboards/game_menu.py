from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from XOgame import field
from .callback import stroke

def create_game_menu():
    kb_game = InlineKeyboardMarkup(row_width=2)

    btn_1 = InlineKeyboardButton(text=field[0],
                                 callback_data=stroke.new(mark='user_stroke', field_num=0))
    btn_2 = InlineKeyboardButton(text=field[1],
                                 callback_data=stroke.new(mark='user_stroke', field_num=1))
    btn_3 = InlineKeyboardButton(text=field[2],
                                 callback_data=stroke.new(mark='user_stroke', field_num=2))
    btn_4 = InlineKeyboardButton(text=field[3],
                                 callback_data=stroke.new(mark='user_stroke', field_num=3))
    btn_5 = InlineKeyboardButton(text=field[4],
                                 callback_data=stroke.new(mark='user_stroke', field_num=4))
    btn_6 = InlineKeyboardButton(text=field[5],
                                 callback_data=stroke.new(mark='user_stroke', field_num=5))
    btn_7 = InlineKeyboardButton(text=field[6],
                                 callback_data=stroke.new(mark='user_stroke', field_num=6))
    btn_8 = InlineKeyboardButton(text=field[7],
                                 callback_data=stroke.new(mark='user_stroke', field_num=7))
    btn_9 = InlineKeyboardButton(text=field[8],
                                 callback_data=stroke.new(mark='user_stroke', field_num=8))
    btn_back = InlineKeyboardButton(text='назад в главное меню',
                                 callback_data=stroke.new(mark='back', field_num=9))
    kb_game.row(btn_1, btn_2, btn_3)
    kb_game.row(btn_4, btn_5, btn_6)
    kb_game.row(btn_7, btn_8, btn_9)
    kb_game.row(btn_back)

    return kb_game

