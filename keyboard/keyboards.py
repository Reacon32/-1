from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton('Отправь туториал по созданию папки на рабочем столе')
    button_2 = KeyboardButton('Перейти на следующую клавиатуру')
    keyboard.add(button_1, button_2)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_3 = KeyboardButton('Покажи смешное видео про волка')
    button_4 = KeyboardButton('Вернуться на предыдущую клавиатуру')
    keyboard_2.add(button_3, button_4)
    return keyboard_2