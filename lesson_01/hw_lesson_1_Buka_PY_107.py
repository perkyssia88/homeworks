# Ex 1
# последовательно просим пользователя ввести 2 integer, string, и float
# num_1 и num_2 из string переводим в integer
# text не трогаем, ф-ция input всегда возвращает string
# float_num переводим из string во float
num_1, num_2, text, float_num = int(input("Введите целое число: ")), int(input("Введите целое число: ")), input(
    "Введите текст: "), float(input("Введите дробное число: "))
# Последовательно выводим сначала string, потом 2 integer и float, каждое с новой строки
print(text, num_1, num_2, float_num, sep="\n")

# Ex 2
# создаем переменные согласно условия задачи
integer_variable, float_variable, bool_variable, string_variable = 1988, 3.11, True, "Just some text"
# преобразуем переменные integer, float в string
integer_variable, float_variable = str(integer_variable), str(float_variable)
# выводим на печать каждую переменную с новой строки
print(integer_variable, float_variable, bool_variable, string_variable, sep="\n")
# проверяем типы переменных
print(type(integer_variable), type(float_variable), type(bool_variable), type(string_variable))