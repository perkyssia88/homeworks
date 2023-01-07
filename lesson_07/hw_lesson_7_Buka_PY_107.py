from math import sqrt  # for ex_1
from random import randint  # for ex_3

# Ex_1 Гипотенуза по длине катетов
leg_1 = float(input("Введите длину катета 1: "))
leg_2 = float(input("Введите длину катета 2: "))
print(f"Длинна гипотенузы будет равна {sqrt(leg_1 ** 2 + leg_2 ** 2)}")

# Ex_2 Среднее из трех чисел
num_1 = float(input("Введите число 1: "))
num_2 = float(input("Введите число 2: "))
num_3 = float(input("Введите число 3: "))
if num_1 < num_2 < num_3:
    print(f"Среднее по значению число - {num_2}")
elif num_3 < num_1 < num_2:
    print(f"Среднее по значению число - {num_1}")
elif num_2 < num_3 < num_1:
    print(f"Среднее по значению число - {num_3}")
elif num_1 == num_2 == num_3:
    print("Все числа равны")
else:
    print("Два числа равны")

# Ex_3 Четное/ нечетное из случайных чисел
rand_num1 = randint(1, 100)
rand_num2 = randint(1, 100)
if rand_num1 % 2 != 0 and rand_num2 % 2 != 0:
    print("Оба числа нечетные")
    print(f"Выпали числа {rand_num1} и {rand_num2}")
elif rand_num1 % 2 == 0 and rand_num2 % 2 == 0:
    print("Оба числа четные")
    print(f"Выпали числа {rand_num1} и {rand_num2}")
elif rand_num1 % 2 == 0 and rand_num2 % 2 != 0:
    print(f"Нечетное число - {rand_num2}")
    print(f"Выпали числа {rand_num1} и {rand_num2}")
else:
    print(f"Нечетное число - {rand_num1}")
    print(f"Выпали числа {rand_num1} и {rand_num2}")

# Ex_4 Перевернуть число(решил переворачивать строку и приводить его к числу)
user_num = input("Введите число: ")
new_num = int(user_num[::-1])
print(new_num)

# Ex_5 Прямоугольник
symb_1 = input("Введите символ: ")
symb_2 = input("Введите второй символ: ")
for i in range(5):
    if i == 0 or i == 4:
        for _ in range(10):
            print(symb_1, end="")
    else:
        print(symb_1, end="")
        for _ in range(1, 9):
            print(symb_2, end="")
        print(symb_1, end="")
    print()

# Ex_6 Совершенные числа от 1 до 10к
for i in range(1, 10001):
    count = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            count += j
    if count == i:
        print(f"Число {i} - совершенное")

# Ex_7 Работа со списком
lst = []
for i in range(10):
    count = (int(input("Введите число: ")))
    if i == 9:
        continue
    lst.append(count)
print(lst)
last_num = int(input("Введите число: "))
num_index = int(input("Введите индекс числа: "))
lst.insert(num_index, last_num)
print(lst)

# Ex_8 Количество слов в предложении
# Добавил метод strip() чтобы убрать возможные пробелы в начале и конце строки
string = input("Введите предложение с одним пробелом между словами: ").strip()
print(f"В вашем предложении {string.count(' ') + 1} слов(а).")

# Ex_9 Убрать все заглавные буквы
string_1 = "HSDsgscajJKYpython"  # можно сделать input("...")
new_string = ""
for i in string_1:
    if i == i.lower():
        new_string += i
print(new_string)

# Ex_10 Вывести числа от 1 до 100 кратные 7
for i in range(7, 101, 7):
    print(i)

# Ex_11 Сложить числа от 1 до 100
count = 0
# от 1 до 100 включительно
for i in range(1, 101):
    count += i
print(count)

# Ex_12 Факториал числа без  math
num_in = int(input("Введите число: "))
factorial = 1
for i in range(1, num_in + 1):
    factorial *= i
print(factorial)

# Ex_13 Ёлочка из чисел последовательности
# Заставила задача подумать, 5+ кто ее придумал)
# запрашиваем пользовательский ввод, str в int
num_input = int(input("Введите число: "))
out_digit = 1  # число последовательности (выводимое в елочку)
str_digit = 1  # количество символов в строке
# пока число последовательности <=  введенному числу
# выполнием цикл
while out_digit <= num_input:
    # создаем вложеный цикл в диапазоне от 1
    # до количество символов в строке + 1 (включая)
    for _ in range(1, str_digit + 1):
        # если число последовательности все еще <= введонномого числа
        # иначе будем в елочку записывать цифры за пределами вводимого числа
        if out_digit <= num_input:
            # выводим на печать ч.п с пробелом в конце
            print(out_digit, end=" ")
            # прибавляем к числу последовательности 1
            out_digit += 1
    # переводим каретку на навую строку
    print()
    # прибавляем к числу количества строк 1
    str_digit += 1
# переходим к следующей итерации цикла while,
# пока его условие не выполнится

# Ex_14 Целые степени двойки
n = int(input("Введите число: "))
count = 1
for i in range(0, n + 1):
    count = 2 ** i
    if count <= n:
        print(f"{count}")
