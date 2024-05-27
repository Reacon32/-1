from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://youtu.be/Jrg9KxGNeJY?si=qLCQF4wlRD8vDBZp')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inline2():
    keyboard_inline2 = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://youtu.be/BEJ91RVfDZY?si=Es7-YwOQMBFQGfh4')
    keyboard_inline2.add(but_inline)
    return keyboard_inline2