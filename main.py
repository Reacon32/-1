from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline, get_keyboard_inline2
from database.database import initialize_db, add_user, get_user

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда запуска бота'),
        types.BotCommand(command='/help', description='Команда для информации о боте'),
        types.BotCommand(command='/command1', description='Тестовая команда 1'),
        types.BotCommand(command='/command2', description='Тестовая команда 2'),
        types.BotCommand(command='/command3', description='Тестовая команда 3'),
        types.BotCommand(command='/command4', description='Тестовая команда 4')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет, я тест бот для первого задания', reply_markup=get_keyboard_1())
    else:
        await message.answer('Привет, я тест бот для первого задания', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь туториал по созданию папки на рабочем столе')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.ytimg.com/vi/5QZcOugHQ6s/maxresdefault.jpg', caption= 'Вот туториал', reply_markup= get_keyboard_inline2())

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Здесь можно попросить смешное видео', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Покажи смешное видео про волка')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.ytimg.com/vi/5OWOQF3dWi0/maxresdefault.jpg', caption= 'Вот твой улыбающийся волк', reply_markup= get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Вернуться на предыдущую клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Здесь можно попросить отправить туториал по созданию папки на рабочем столе', reply_markup= get_keyboard_1())

@dp.message_handler(commands= 'help')
async def start(message: types.Message):
    await message.reply('Чем я могу помочь тебе?')

@dp.message_handler(commands= 'command1')
async def start(message: types.Message):
    await message.reply('Тестовая команда 1')

@dp.message_handler(commands= 'command2')
async def start(message: types.Message):
    await message.reply('Тестовая команда 2')

@dp.message_handler(commands= 'command3')
async def start(message: types.Message):
    await message.reply('Тестовая команда 3')

@dp.message_handler(commands= 'command4')
async def start(message: types.Message):
    await message.reply('Тестовая команда 4')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
