from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton('Отправить видео по основам Blender')
    button_2 = KeyboardButton('Перейти на следующий туториал')
    keyboard.add(button_1, button_2)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_3 = KeyboardButton('Отправить видео по первому проекту в Blender')
    button_4 = KeyboardButton('Вернуться на предыдущий туторил')
    keyboard_2.add(button_3, button_4)
    return keyboard_2