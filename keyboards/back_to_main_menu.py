from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback import stroke


kb_back = InlineKeyboardMarkup(row_width=2)
btn_back = InlineKeyboardButton(text='назад в главное меню',
                                callback_data=stroke.new(mark='back', field_num=9))
kb_back.row(btn_back)