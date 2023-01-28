from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

basis = ReplyKeyboardMarkup(resize_keyboard=True)
info = KeyboardButton("Информация")
bibliography = KeyboardButton("Список полезной литературы")
basis.add(info, bibliography)


bibliography_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("Git. Практическое руководство")
button2 = KeyboardButton("Python - Crash Course")
button3 = KeyboardButton("Python True Book")
button4 = KeyboardButton("Python. Сборник упражнений")
button5 = KeyboardButton("SQL.Сборник рецептов")
button6 = KeyboardButton("Марк Лутц - изучаем Python")
button7 = KeyboardButton("<-- Назад")
bibliography_keyboard.add(button1, button2, button3,
                          button4, button5, button6,
                          button7)


info_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("О Python")
button2 = KeyboardButton("О боте")
button3 = KeyboardButton("Что может бот")
button4 = KeyboardButton("Самое интересное")
button5 = KeyboardButton("<-- Назад")
info_keyboard.add(button1, button2, button3,
                  button4, button5)