from random import randint  # for Ex_3


# Ex_1 количество разрядов числа
def len_1(a): return len(str(a))


num = input("Введите число: ")
print("Вариант 1 - через строки:  ")
print(f"В числе {num} - {len_1(num)} разряда(ов)\n")


# Ex_1_v.2.0 количество разрядов числа
def len_2(a):
    count = 0
    while a > 0:
        a = a // 10
        count += 1
    return count


num = int(input("Введите число: "))
print("Вариант 2 - через цикл while: ")
print(f"В числе {num} - {len_2(num)} разряда(ов)\n")


# Ex_1_v.3.0 количество разрядов числа
def len_3(a):
    if a > 0:
        count = len_3(a // 10)
        count += 1
        return count
    else:
        return 0


num = int(input("Введите число: "))
print("Вариант 3 - через рекурсивную функцию: ")
print(f"В числе {num} - {len_3(num)} разряда(ов)\n")


# Ex_2 площадь круга, прямоугольника и треугольника
# за основу взят прямоугольный треугольник
def sqr_circle(a=1):
    s = 3.14 * a ** 2
    return s


def sqr_rectangle(a=1, b=1):
    s = a * b
    return s


def sqr_triangle(a, b):
    s = a * b / 2
    return s


geom_config = input(f"Введите: \n"
                    f"1 - для вычисления площади круга \n"
                    f"2 - для вычисления площади прямоугольника \n"
                    f"3 - для вычисления площади прямоугольного треугольника \n")

match geom_config:
    case "1":
        radius = float(input("Введите радиус круга: "))
        print(f"Площадь круга с радиусом {radius} равна {sqr_circle(radius)}")
    case "2":
        length = float(input("Введите длину прямоугольника: "))
        height = float(input("Введите высоту прямоугольника: "))
        print(f"Площадь прямоугольника с длиной - {length} и"
              f" высотой - {height} равна {sqr_rectangle(length, height)}")
    case "3":
        leg_1 = float(input("Введите длину катета 1: "))
        leg_2 = float(input("Введите длину катета 2: "))
        print(f"Площадь прямоугольного треугольника с катетами {leg_1} "
              f"и {leg_2} равна {sqr_triangle(leg_1, leg_2)}")
    case _:
        print(f"Введено неверное значение")


# Ex_3 функция заполнения списка 10 случайными числами
def get_list(a, b):
    lst = [randint(a, b) for _ in range(10)]
    print(lst)  # для проверки


num_start = int(input("Введите число начала диапозона: "))
num_end = int(input("Введите число конца диапозона: "))
get_list(num_start, num_end)


# Ex_4 секунды в формате дни:часы:минуты:секунды
def get_time(a):
    while a > 0:
        sec_ = a % 60  # 60
        min_ = a % 3600 // 60  # 180
        hour_ = a % 86400 // 3600  # 3600
        days_ = a // 86400  # 86400
        return print(f"{days_}:{hour_}:{min_}:{sec_}")


seconds = int(input("Введите количество секунд: "))
get_time(seconds)


# Ex_5 получить количество гласных и согласных в строке
def get_vow_and_cons(a):
    vowels = 0
    consonant = 0
    not_letters = 0
    for _ in a.lower():
        if _ in "aeiouy":
            vowels += 1
        elif _ in "bcdfghjklmnpqrstvwxz":
            consonant += 1
        else:
            not_letters += 1
    return f"Во введенной строке {vowels} - гласных, " \
           f"{consonant} согласных и {not_letters} не буквенных символов"


str_input = input("Введите строку: ")
print(get_vow_and_cons(str_input))


# Ex_6 n + nn + nnn
def n(a):
    num_1 = a
    num_2 = a * 2
    num_3 = a * 3

    num_ = int(num_1) + int(num_2) + int(num_3)
    return num_


input_num = input("Введите число: ")
print(n(input_num))


# Ex_7
def math_func(a):
    if -5 <= a <= 5:
        return a ** 2
    elif a < -5:
        return 2 * abs(a) - 1
    else:
        return 2 * a


for i in range(-10, 11):
    print(f"Число - {i}, результат работы функции - {math_func(i)}")


# Homework
def func(a):
    # tuple
    if isinstance(a, tuple):
        count = 0
        for _ in a:
            if isinstance(_, str):
                count += len(_)
        return f"В кортеже длина всех слов равна {count} символов."
    # list
    elif isinstance(a, list):
        letters = 0
        numbers = 0
        for _ in a:
            if isinstance(_, str):
                letters += len(_)
            elif isinstance(_, int):
                numbers += 1
        return f"В списке {letters} букв и {numbers} цифр."
    # integer
    elif isinstance(a, int):
        odd_nums = 0
        for _ in str(a):
            if int(_) % 2 == 1:
                odd_nums += 1
        return f"В числе {odd_nums} нечетных цифр."
    # string
    elif isinstance(a, str):
        return f"В строке {len(a)} букв включая пробелы и знаки препинания."


# tuple
print(func((1, 5, "hello", "world", 20.5, "geksometilenatriperoksiddiamin", True, [1, 2, 3])))
# list
print(func([1, 5, "hello", "world", 20.5, "geksometilenatriperoksiddiamin",
            True, [1, 2, 3]]))
# integer
print(func(1921681125525500))  # 9 odd_nums
# string
print(func(f"Разбираем каждый себе тему."
           f"Дедлайн - следующий понедельник"))  # 58
