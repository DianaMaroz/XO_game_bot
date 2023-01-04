from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b3 = KeyboardButton('/орел')
b4 = KeyboardButton('/решка')

kb_turn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_turn.add(b3).insert(b4)