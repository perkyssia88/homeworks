# Ex_1
# создаем переменную для перемножения
total = 1
# запускаем цикл по условию от [1 до 100]
for i in range(1, 101):
    # создаем условие: если остаток от деления переменной цикла НЕ равен 0
    if i % 2 != 0:
        # то производим перемножение переменной перемножения
        # и переменной цикла
        total *= i
# выводим итоговый результат работы цикла
print(total)

# Ex_2
# создаем пустой массив(array, list, список)
arr_ = []
# запускием цикл по условию от [1 до 500]
for i in range(1, 501):
    # если остаток от деления переменний цикла равен 0
    if i % 5 == 0:
        # добавляем значение переменной цикла в конец массива arr_
        arr_.append(i)
# выводим на печать итоговый результат работы цикла
print(arr_)

# Ex_3
# создаем цикл по условию от [1 до 497]
for i in range(1, 498):
    # если остаток от деления переменной цикла равен 0
    if i % 2 == 0:
        # выводим на экран значение переменной цикла
        print(i)

# Ex_4
# дан массив чисел, кто знает, тот поймет))
lst = [192, 168, 1, 1, 255, 255, 255, 0]
# создаем новый постой список(он же массив, хранить будем только числа)
new_lst = []
# создаем цикл с переменной i для проверки всех объектов внутри списка
for i in lst:
    # если количество повторений переменной i в списке больше или равно 2
    if lst.count(i) >= 2:
        # если переменная i еще не присутствует в новом списке
        if i not in new_lst:
            # добавляем переменную i в конец нового списка
            new_lst.append(i)
# распечатываем итоговое значение переменной new_lst
print(new_lst)

# Ex_5 Творческое
# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит натуральное число из отрезка [a:b]с максимальной суммой делителей.
# Программа должна вывести два числа на одной строке,
# разделенных пробелом: число с максимальной суммой делителей и сумму его делителей.
# запрашиваем пользовательский ввод и преобразуем из str в int
user_input_1 = int(input("Введите первое число: "))
# запрашиваем пользовательский ввод и преобразуем из str в int
user_input_2 = int(input("Введите второе число, большее первого: "))
# создаем переменную суммы делителей
total = 0
# создаем переменную числа с максимальной суммой делителей
max_digit = 0
# создаем условие что пользователь ввел второе число больше чем первое
if user_input_1 < user_input_2:
    # создаем цикл в диапазоне от 1-го до 2-го чисел пользовательского ввода включительно
    for i in range(user_input_1, user_input_2 + 1):
        # создаем счетчик первого цикла со значением 0 (суммы делителей)
        count = 0
        # создаем второй цикл в диапазоне от 1 до числа переменной первого цикла включительно.
        # не от 0, т.к на 0 делить нельзя))).
        for j in range(1, i + 1):
            # если переменная первого цикла(пользовательского ввода)
            # делится без остатка на переменную второго цикла
            if i % j == 0:
                # то добавляем к счетчику суммы делителей значение перменной второго цикла
                # (делитель числа первого цикла)
                count += j
            # если сумма делителей больше или равна переменной суммы делителей предыдущих итераций.
            # и переменная первого цикла  больше предыдущих итераций.
            if count >= total and i >= max_digit:
                # то переменная суммы делителей приравнивается к счетчику суммы делителей
                total = count
                # а переменная числа с максимальной суммой делителей
                # приравнивается к числу данной итерации цикла 1
                max_digit = i
# если числа пользовательского ввода равны - не соблюдено условие задачи
elif user_input_1 == user_input_2:
    print("Введенные числа равны, попробуйте снова...")
else:
    # если первое число больше второго:
    # не соблюдено условие задачи
    print("Первое введенное число меньше второго, попробуйте снова...")
print(f"Число с максимальным количеством делителей {max_digit}, их сумма равна {total}")
