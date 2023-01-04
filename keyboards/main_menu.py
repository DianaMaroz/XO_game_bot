from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
b1 = KeyboardButton('/да')
b2 = KeyboardButton('/нет')


kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.row(b1, b2)