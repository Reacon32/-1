from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline, get_keyboard_inline2, get_keyboard_inline3, get_keyboard_inline4, get_keyboard_inline5, get_keyboard_inline6, get_keyboard_inline7
from database.database import initialize_db, add_user, get_user

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда запуска бота'),
        types.BotCommand(command='/download', description='Команда для скачивания Blender'),
        types.BotCommand(command='/animation', description='Команда с основами анимации'),
        types.BotCommand(command='/shading', description='Команда с основами шейдинга'),
        types.BotCommand(command='/camera', description='Команда с основами камеры'),
        types.BotCommand(command='/sculpting', description='Команда с основами скульптинга')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет, я бот который поможет тебе начать осваивать программму Blender. Зайди в меню справа, чтобы посмотреть видео по основам интерфейса --->', reply_markup=get_keyboard_1())
    else:
        await message.answer('Привет, я бот который поможет тебе начать осваивать программму Blender. Зайди в меню справа, чтобы посмотреть видео по основам интерфейса --->', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправить видео по основам Blender')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo= 'https://i.ytimg.com/vi/h0th3K4Hkc8/maxresdefault.jpg',
                         caption= 'В этом видео можно псмотреть общий функционал и интерфейс Blender',
                         reply_markup= get_keyboard_inline2())

@dp.message_handler(lambda message: message.text == 'Перейти на следующий туториал')
async def button_2_click(message: types.Message):
    await message.answer('Отлично! Теперь когда ты знаешь основы, попробуй создать свой первый проект по видео из меню', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправить видео по первому проекту в Blender')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo= 'https://i.ytimg.com/vi/ryq4Vj7G5NA/maxresdefault.jpg',
                         caption= 'Попробуй смоделировать пончик по этому видео',
                         reply_markup= get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Вернуться на предыдущий туторил')
async def button_4_click(message: types.Message):
    await message.answer('Если у тебя получилось создать пончик, то поздравляю, теперь ты знаешь основные функции Blender. Можешь глянуть парочку интересных роликов в левом меню', reply_markup= get_keyboard_1())

@dp.message_handler(commands= 'download')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo= 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Blender.svg/1200px-Blender.svg.png',
                         caption= 'Если у тебя нет Blender на компьютере, то ты можешь перейти по ссылки для скачивания снизу',
                         reply_markup= get_keyboard_inline3())

@dp.message_handler(commands= 'animation')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo='https://i.ytimg.com/vi/7illSG02d04/maxresdefault.jpg',
                         caption='Курс по анимации в Blender',
                         reply_markup=get_keyboard_inline4())

@dp.message_handler(commands= 'shading')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo='https://i.ytimg.com/vi/Wmbowt6_U7E/maxresdefault.jpg',
                         caption='Курс по шейдингу в Blender',
                         reply_markup=get_keyboard_inline5())

@dp.message_handler(commands= 'camera')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo='https://i.ytimg.com/vi/h2EzclzP_-4/maxresdefault.jpg',
                         caption='Курс по работе с камерой в Blender',
                         reply_markup=get_keyboard_inline6())

@dp.message_handler(commands= 'sculpting')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo='https://i.ytimg.com/vi/hx34Pr9YDZc/maxresdefault.jpg',
                         caption='Курс по скульптингу в Blender',
                         reply_markup=get_keyboard_inline7())

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
