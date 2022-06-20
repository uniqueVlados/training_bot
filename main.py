from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


TOKEN = "5557039981:AAG6q2mgRdjA8M0UTYW9ZRTnx7hrTS56BeA"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# BUTTONS
BUTTON_FORM = KeyboardButton('Ввести свои данные📄')

BUTTON_GENDER = KeyboardButton('ПОЛ👧👦')f
BUTTON_AGE = KeyboardButton('ВОЗРАСТ👱‍♂️🧔🧓')
BUTTON_HEIGHT = KeyboardButton('РОСТ👤')
BUTTON_WEIGHT = KeyboardButton('ВЕС👤')

BUTTON_MAN = KeyboardButton('М👦')
BUTTON_WOMAN = KeyboardButton('Ж👧')

BUTTON_PROGRAM = KeyboardButton('Подобрать программу📒')

BUTTON_GOAL1 = KeyboardButton('1️⃣')
BUTTON_GOAL2 = KeyboardButton('2️⃣')
BUTTON_GOAL3 = KeyboardButton('3️⃣')
BUTTON_GOAL4 = KeyboardButton('4️⃣')
BUTTON_GOAL5 = KeyboardButton('5️⃣')
BUTTON_GOAL6 = KeyboardButton('6️⃣')

BUTTON_TIME2 = KeyboardButton('1️⃣ раз')
BUTTON_TIME3 = KeyboardButton('3️⃣ раза ')
BUTTON_TIME4 = KeyboardButton('4️⃣ раза')
BUTTON_TIME5 = KeyboardButton('5️⃣ раз')
BUTTON_TIME6 = KeyboardButton('6️⃣ раз')

# KEYBOARDS
KB_START = ReplyKeyboardMarkup(resize_keyboard=True)
KB_START.add(BUTTON_FORM)

KB_INPUT_FORM = ReplyKeyboardMarkup(resize_keyboard=True)
KB_INPUT_FORM.add(BUTTON_GENDER, BUTTON_AGE, BUTTON_HEIGHT, BUTTON_WEIGHT)

KB_GENDER = ReplyKeyboardMarkup(resize_keyboard=True)
KB_GENDER.add(BUTTON_MAN, BUTTON_WOMAN)

KB_PROGRAM = ReplyKeyboardMarkup(resize_keyboard=True)
KB_PROGRAM.add(BUTTON_PROGRAM)

KB_GOAL = ReplyKeyboardMarkup(resize_keyboard=True)
KB_GOAL.add(BUTTON_GOAL1, BUTTON_GOAL2, BUTTON_GOAL3, BUTTON_GOAL4, BUTTON_GOAL5, BUTTON_GOAL6)

KB_TIME = ReplyKeyboardMarkup(resize_keyboard=True)
KB_TIME.add(BUTTON_TIME2, BUTTON_TIME3, BUTTON_TIME4, BUTTON_TIME5, BUTTON_TIME6)


STATES = {}
STATES_FORM = {}


GOAL1 = "1️⃣ Сжигание жира  и мышечный рельеф (параллельно + выносливость, сила, гибкость, улучшение качества жизни, замедление старения)."
GOAL2 = "2️⃣ Набор мышечной массы и увеличение силы (параллельно + выносливость, сила, гибкость, улучшение качества жизни, замедление старения)."
GOAL3 = "3️⃣ Оздоровление и улучшение самочувствия и основных показателей прочности организма - максимальное потребление кислорода (параллельно + выносливость, сила, гибкость, улучшение качества жизни, замедление старения)"
GOAL4 = "4️⃣ Спорт: любительский или профессиональный?"
GOAL5 = "5️⃣ Профилактика травм и восстановление (индивидуальные консультации)."
GOAL6 = "6️⃣ Зарядка энергией по утрам на каждый день"


@dp.message_handler(commands=['start'])
async def start_(message: types.Message):
    STATES.clear()
    STATES_FORM.clear()
    user_id = str(message.from_user.id)
    STATES[user_id] = {'G': None, 'A': None, 'H': None, 'W': None}
    STATES_FORM[user_id] = {'G': 0, 'A': 0, 'H': 0, 'W': 0}
    await message.reply(f"Здравствуйте, {message.from_user.first_name}\nПеред началом подбора программы воспользуйтесб кнопкой ниже "
                        f"и введите свои данные⬇️", reply_markup=KB_START)


# @dp.message_handler(commands=['help'])
# async def start_(message: types.Message):
#     await message.reply(HELP_INFO, reply_markup=KB_PROJECT, parse_mode="Markdown")


@dp.message_handler()
async def info(message: types.Message):
    user_id = str(message.from_user.id)
    if message.text == "Ввести свои данные📄":
        await message.reply("⬇️КНОПКИ ДЛЯ ЗАПОЛНЕНИЯ⬇️", reply_markup=KB_INPUT_FORM)

    # -------
    if message.text == 'ПОЛ👧👦':
        await message.reply("Выберите ниже⬇️", reply_markup=KB_GENDER)
    if message.text == 'М👦':
        STATES[user_id]['G'] = "M"
        STATES_FORM[user_id]['G'] = 1
        await message.reply("Спасибо. Запомнили. Продолжаем дальше⬇️", reply_markup=KB_INPUT_FORM)
        if STATES[user_id]['G'] is not None and STATES[user_id]['A'] is not None and STATES[user_id]['H'] is not None and STATES[user_id]['W'] is not None:
            await message.reply("Вы ввели все данные. Нажмите ниже, чтобы подобрать программу⬇️", reply_markup=KB_PROGRAM)
    if message.text == 'Ж👧':
        STATES[user_id]['G'] = "W"
        STATES_FORM[user_id]['G'] = 1
        await message.reply("Спасибо. Запомнили. Продолжаем дальше⬇️", reply_markup=KB_INPUT_FORM)

    # ------
    if STATES_FORM[user_id]['A'] == 1:
        STATES[user_id]['A'] = message.text
        STATES_FORM[user_id]['A'] = 0
        await message.reply("Спасибо. Запомнили. Продолжаем дальше⬇️", reply_markup=KB_INPUT_FORM)
        if STATES[user_id]['G'] is not None and STATES[user_id]['A'] is not None and STATES[user_id]['H'] is not None and STATES[user_id]['W'] is not None:
            await message.reply("Вы ввели все данные. Нажмите ниже, чтобы подобрать программу⬇️", reply_markup=KB_PROGRAM)
    if message.text == 'ВОЗРАСТ👱‍♂️🧔🧓':
        STATES_FORM[user_id]['A'] = 1
        await message.reply("Введите целое количество лет ниже⬇️", reply_markup=KB_INPUT_FORM)

    # ------
    if STATES_FORM[user_id]['H'] == 1:
        STATES[user_id]['H'] = message.text
        STATES_FORM[user_id]['H'] = 0
        await message.reply("Спасибо. Запомнили. Продолжаем дальше⬇️", reply_markup=KB_INPUT_FORM)
        if STATES[user_id]['G'] is not None and STATES[user_id]['A'] is not None and STATES[user_id]['H'] is not None and STATES[user_id]['W'] is not None:
            await message.reply("Вы ввели все данные. Нажмите ниже, чтобы подобрать программу⬇️", reply_markup=KB_PROGRAM)
    if message.text == 'РОСТ👤':
        STATES_FORM[user_id]['H'] = 1
        await message.reply("Введите рост ниже\nПример(1м 78см)⬇️", reply_markup=KB_INPUT_FORM)

    # ------
    if STATES_FORM[user_id]['W'] == 1:
        STATES[user_id]['W'] = message.text
        STATES_FORM[user_id]['W'] = 0
        await message.reply("Спасибо. Запомнили. Продолжаем дальше⬇️", reply_markup=KB_INPUT_FORM)
        if STATES[user_id]['G'] is not None and STATES[user_id]['A'] is not None and STATES[user_id]['H'] is not None and STATES[user_id]['W'] is not None:
            await message.reply("Вы ввели все данные. Нажмите ниже, чтобы подобрать программу⬇️", reply_markup=KB_PROGRAM)

    if message.text == 'ВЕС👤':
        STATES_FORM[user_id]['W'] = 1
        await message.reply("Введите вес ниже\nПример(76кг)⬇️", reply_markup=KB_INPUT_FORM)

    # ------
    if message.text == 'Подобрать программу📒':
        await message.reply(f"{GOAL1}\n\n{GOAL2}\n\n{GOAL3}\n\n{GOAL4}\n\n{GOAL5}\n\n{GOAL6}", reply_markup=KB_GOAL)

    # -----
    if message.text == '1️⃣' or message.text == '2️⃣' or message.text == '3️⃣' or message.text == '4️⃣':
        await message.reply("Cколько раз в неделю планируете заниматься. Выберете вариант ниже⬇️", reply_markup=KB_TIME)

    print(STATES)
    print(STATES_FORM)




if __name__ == '__main__':
    executor.start_polling(dp)

