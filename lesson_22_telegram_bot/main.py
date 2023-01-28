import logging
import asyncio
import config
import keyboard
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

"""Реализуйте телеграмм-бота с двумя inline кнопками
(информация, список полезной литературы для
разработчиков на языке Python)"""

# proxy_url = "http://proxy.server:3128"
storage = MemoryStorage()
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)  # proxy=proxy_url
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(filename="log.txt", level=logging.INFO,
                    format=u"%(filename)s [LINE:%(lineno)d #%(levelname)-8s] %(message)s")


@dp.message_handler(Command("start"), state=None)
async def welcome(message):
    __file = open("user.txt", "r")
    __users = set()
    for line in __file:
        __users.add(line.strip())

    if not str(message.chat.id) in __users:
        __file = open("user.txt", "a")
        __file.write(str(message.chat.id) + "\n")
        __users.add(message.chat.id)

    await bot.send_message(message.chat.id, f"Привет, *{message.from_user.first_name}*, я к работе готов!))",
                           reply_markup=keyboard.basis, parse_mode="Markdown")


@dp.message_handler(content_types=["text"])
async def get_message(message):
    __link_list = ["https://drive.google.com/file/d/1buXiPkhldRXBlUllNRt8lP7D4Xv6AVuB/view?usp=share_link",
                   "https://drive.google.com/file/d/1_EqVJpZDDL_3kPiCcFwZP-ilD3s7fAWU/view?usp=share_link",
                   "https://drive.google.com/file/d/1yaRhNzGJUm9HQxHqBBMgmuma-3CJ0ksZ/view?usp=share_link",
                   "https://drive.google.com/file/d/148lV3kPNePkDdjhQcLzlCBmj2rGA940r/view?usp=share_link",
                   "https://drive.google.com/file/d/1ZZRPNsqBxtEy5qFGAMcimEcw5Ai81b4F/view?usp=share_link",
                   "https://drive.google.com/file/d/1wC_XTn3Ga-PFy8fJtBO7toNIeCj-2rcQ/view?usp=share_link"]
    match message.text:
        case "Информация":
            await bot.send_message(message.chat.id, text="Информация по Python",
                                   reply_markup=keyboard.info_keyboard, parse_mode="Markdown")
        case "Список полезной литературы":
            await bot.send_message(message.chat.id, f"Вот список полезной литературы для изучения Python",
                                   reply_markup=keyboard.bibliography_keyboard, parse_mode="Markdown")
        case "Git. Практическое руководство":
            await bot.send_message(message.chat.id, text="Данная книга представляет собой подробное практическое "
                                                         "руководство по Git, в котором описывается Git и приводится "
                                                         "разбор конкретных ситуаций и применений, например , как "
                                                         "изменения из одной ветки разработки включить в другую ветку, "
                                                         "но не все. Изложение начинается с самых азов, никакой "
                                                         "предварительной подготовки не требуется: по ходу изложения "
                                                         "даются все необходимые определения и пояснения.")
            await bot.send_message(message.chat.id, text=__link_list[0])
        case "Python - Crash Course":
            await bot.send_message(message.chat.id, text="В книге рассматриваются все основные темы необходимые для "
                                                         "Python-разработчика, от основ Python, до работы с данными, "
                                                         "Django и Web приложениями в целом. *Язык книги - английский*",
                                   parse_mode="Markdown")
            await bot.send_message(message.chat.id, text=__link_list[1])
        case "Python True Book":
            await bot.send_message(message.chat.id, text="В книге представлены более темы для более глубокого "
                                                         "погружения в разработку на языке Python, рассматриваются "
                                                         "такие темы как: работа с csv, word, pdf файлами, основы - "
                                                         "HTML, машинного обучения, автоматического тестирования и "
                                                         "методов отладки. Подразумевается владения базовыми навыками "
                                                         "программирования на языке Python. *Язык книги - английский*",
                                   parse_mode="Markdown")
            await bot.send_message(message.chat.id, text=__link_list[2])
        case "Python. Сборник упражнений":
            await bot.send_message(message.chat.id, text="Сборник содержит 186 задач по программированию разной степени"
                                                         " сложности. Для ряда упражнений изложены решения с подробным"
                                                         " разбором фрагментов кода и синтаксических конструкций языка"
                                                         " Python. В книге представлен простой и понятный стиль "
                                                         "программирования. Чтобы решить приведенные здесь задачи, "
                                                         "достаточно базовых знаний языка Python. По мере изучения "
                                                         "материала читатель отрабатывает навык использования таких "
                                                         "техник, как условные выражения, циклы, основные функции, "
                                                         "списки, словари, рекурсия и работа с файлами.")
            await bot.send_message(message.chat.id, text=__link_list[3])
        case "SQL.Сборник рецептов":
            await bot.send_message(message.chat.id, text="Рассмотрены готовые рецепты для решения практических задач "
                                                         "при работе с СУБД Oracle, 082, SQL Server, MySQL и "
                                                         "PostgreSQL. Описаны извлечение записей из таблиц, сортировка "
                                                         "результатов запросов, принципы работы с несколькими "
                                                         "таблицами, обработка запросов с метаданными. Рассказывается о"
                                                         " способах поиска данных средствами SQL, о составлении отчетов"
                                                         " и форматировании результирующих множеств, работе с "
                                                         "иерархическими запросами и многое другое.")
            await bot.send_message(message.chat.id, text=__link_list[4])
        case "Марк Лутц - изучаем Python":
            await bot.send_message(message.chat.id, text="Можно сказать легендарная книга Марка Лутца для изучения "
                                                         "основ Python в 5-м издании на 2019 год, рассматриваются все "
                                                         "основные темы включая очень подробное рассмотрение ООП. Можно"
                                                         " использовать как карманный справочник")
            await bot.send_message(message.chat.id, text=__link_list[5])
        case "<-- Назад":
            await bot.send_message(message.chat.id, f"Выберите интересующий пункт меню",
                                   reply_markup=keyboard.basis, parse_mode="Markdown")
        case "О Python":
            await bot.send_message(message.chat.id, "*Python* - это высокоуровневый, объектно-ориентированный, "
                                                    "интерпретируемый язык программирования с "
                                                    "динамической типизацией", parse_mode="Markdown")
        case "О боте":
            await bot.send_message(message.chat.id, "Данный бот создан в образовательных целях, "
                                                    "с минимальным набором функций, по мере развития "
                                                    "навыков будет улучшаться, развиваться и увеличивать "
                                                    "свой функционал")
        case "Что может бот":
            await bot.send_message(message.chat.id, "В данный момент бот может выводить информацию о себе, своих "
                                                    "возможностях, а так же через \"Список полезной литературы\" "
                                                    "предоставлять ссылки на выбранные книги")
        case "Самое интересное":
            await bot.send_message(message.chat.id, "https://docs.python.org/3/")


if __name__ == "__main__":
    print("+")
    executor.start_polling(dp, skip_updates=True)
