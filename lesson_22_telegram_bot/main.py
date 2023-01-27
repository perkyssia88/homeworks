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

storage = MemoryStorage()
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
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

    await bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}, я к работе готов!))",
                           reply_markup=keyboard.basis, parse_mode="Markdown")


@dp.message_handler(content_types=["text"])
async def get_message(message):
    text1 = "Информация по Python"
    __link_list = ["https://drive.google.com/file/d/1buXiPkhldRXBlUllNRt8lP7D4Xv6AVuB/view?usp=share_link",
                   "https://drive.google.com/file/d/1_EqVJpZDDL_3kPiCcFwZP-ilD3s7fAWU/view?usp=share_link",
                   "https://drive.google.com/file/d/1yaRhNzGJUm9HQxHqBBMgmuma-3CJ0ksZ/view?usp=share_link",
                   "https://drive.google.com/file/d/148lV3kPNePkDdjhQcLzlCBmj2rGA940r/view?usp=share_link",
                   "https://drive.google.com/file/d/1ZZRPNsqBxtEy5qFGAMcimEcw5Ai81b4F/view?usp=share_link",
                   "https://drive.google.com/file/d/1wC_XTn3Ga-PFy8fJtBO7toNIeCj-2rcQ/view?usp=share_link"]
    match message.text:
        case "Информация":
            await bot.send_message(message.chat.id, text=text1,
                                   reply_markup=keyboard.info_keyboard, parse_mode="Markdown")
        case "Список полезной литературы":
            await bot.send_message(message.chat.id, f"Вот список полезной литературы для изучения Python",
                                   reply_markup=keyboard.bibliography_keyboard, parse_mode="Markdown")
        case "Git. Практическое руководство":
            await bot.send_message(message.chat.id, text=__link_list[0], parse_mode="HTML")
        case "Python - Crash Course":
            await bot.send_message(message.chat.id, text=__link_list[1], parse_mode="HTML")
        case "Python True Book":
            await bot.send_message(message.chat.id, text=__link_list[2], parse_mode="HTML")
        case "Python. Сборник упражнений":
            await bot.send_message(message.chat.id, text=__link_list[3], parse_mode="HTML")
        case "SQL.Сборник рецептов":
            await bot.send_message(message.chat.id, text=__link_list[4], parse_mode="HTML")
        case "Марк Лутц - изучаем Python":
            await bot.send_message(message.chat.id, text=__link_list[5], parse_mode="HTML")
        case "<-- Назад":
            await bot.send_message(message.chat.id, f"Выберите интересующий пункт меню",
                                   reply_markup=keyboard.basis, parse_mode="Markdown")


# @dp.message_handler(commands="info")
# async def button_info(message: types.Message):
#     await message.reply("Вывод какой-либо информации")


if __name__ == "__main__":
    print("+")
    executor.start_polling(dp, skip_updates=True)
