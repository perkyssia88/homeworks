# Ex_1 Индекс массы тела
def get_bma(h, w):
    """
    :param h: height
    :param w: weight
    :return: bma index with comment
    """
    bma = round(w / (h / 100) ** 2, 2)
    message = f"Индекс массы тела = {bma} -"
    if 0 < bma <= 16:
        return message + " выраженный дефицит массы тела"
    elif 16 < bma <= 18.5:
        return message + " недостаточная (дефицит) масса тела"
    elif 18.5 < bma <= 25:
        return message + " норма"
    elif 25 < bma <= 30:
        return message + " избыточная масса тела"
    elif 30 < bma <= 35:
        return message + " ожирение 1 степени"
    elif 35 < bma <= 40:
        return message + " ожирение 2 степени"
    elif bma > 40:
        return message + " ожирение 3 степени"
    else:
        return "Введены неверные данные"


height = float(input("Введите ваш рост в сантиметрах: "))
weight = float(input("Введите ваш вес в килограммах: "))
print(get_bma(height, weight))


# Ex_2 Вид фигуры по количеству сторон (как понял условие, так и сделал)
def determine_geom_config(sides):
    geom_config = ["None", "отрезок", "два отрезка", "треугольник",
                   "четырехугольник", "пятиугольник", "шестиугольник",
                   "семиугольник", "восьмиугольник",
                   "девятиугольник", "десятиугольник"]
    if 3 <= sides <= 10:
        return geom_config[sides]
    else:
        return "Введено неверное значение"


sides_num = int(input("Введите количество сторон фигуры от 3 до 10: "))
print(determine_geom_config(sides_num))


# Ex_3 Следующий день за введенной датой
def next_day(input_date):
    days_in_month = {"января": 31, "февраля": 28, "марта": 31, "апреля": 30,
                     "мая": 31, "июня": 30, "июля": 31, "августа": 31,
                     "сентября": 30, "октября": 31, "ноября": 30, "декабря": 31
                     }
    months = [_ for _ in days_in_month]
    day_ = int(input_date[0])
    month_ = input_date[1].lower()
    year_ = int(input_date[2])
    if year_ % 4 == 0 and year_ % 100 != 0 or year_ % 400 == 0:
        days_in_month["февраля"] = 29
    if month_ not in days_in_month or day_ > days_in_month.get(month_):
        return "Неверный формат даты"
    for i, j in days_in_month.items():
        if i == month_ and j > day_:
            return f"Следующий день - {day_ + 1} {month_} {year_}"
        elif i == month_ and i != "декабря" and j == day_:
            return f"Следующий день - 01 {months[months.index(month_) + 1]} {year_}"
        elif i == month_ and i == "декабря" and j == day_:
            return f"Следующий день - 01 {months[0]} {year_ + 1}"


date = input(f"Введите дату (число, месяц (прописью в родительном падеже) "
             f"и год через пробел: ").split(" ")
print(next_day(date))


# Ex_4 Стоимость доставки
def delivery_cost(positions):
    cost = 10.95
    while positions > 1:
        cost += 2.95
        positions -= 1
    return f"Стоимость доставки равна ${round(cost, 2)}"


print(delivery_cost(int(input("Введите количество товаров на доставку: "))))


# Ex_5 Сокращение дроби
def reduce_fraction(a, b):
    """
    :param a: numerator of fraction
    :param b: denominator of fraction
    :return:  reduction of the fraction
    """
    div_a = []
    div_b = []
    for i in range(1, a + 1):
        if a % i == 0:
            div_a.append(i)
    for i in range(1, b + 1):
        if b % i == 0:
            div_b.append(i)
    r = set(div_a) & set(div_b)
    return f"Числитель {int(a / max(r))} - знаменатель {int(b / max(r))}"


num_1 = int(input("Введите числитель дроби: "))
num_2 = int(input("Введите знаменатель дроби: "))
print(reduce_fraction(num_1, num_2))


# Ex_6 Работа со списком (не написано что ф-ция должна что-то возвращать)
def list_func(lst):
    print(f"Изначальный список - {lst}\n")
    print(f"Перевернутый список {lst[::-1]}")
    num_lst = []
    str_lst = []
    for i in lst:
        if isinstance(i, int):
            num_lst.append(i)
        else:
            str_lst.append(i)
    print(f"По возрастанию {sorted(num_lst) + sorted(str_lst, key=len)}")
    print(f"По убыванию {sorted(num_lst, reverse=True) + sorted(str_lst, key=len, reverse=True)}")
    print(f"Срез 2-7 элементы {lst[1:7]}")
    lst_copy = lst.copy()
    del lst_copy[4]
    print(f"С удаленным 5-м элементом {lst_copy}")
    print(f"Без дубликатов {list(set(lst))}")
    print(f"Без чисел {str_lst}")


my_list = [192, "Hello", 168, 0, 1, "world", 255, 255, "python", 1984]
list_func(my_list)


# Ex_7
def count_range(lst, a, b):
    """
    :param lst: list with int & float digits
    :param a: min
    :param b: max
    :return: all digits min <= digit < max
    """
    count = 0
    for i in lst:
        if a <= i < b:
            count += 1
    return count


num_list = [1, 5, 16, 53.3, 53.0, 53, 15, 84, 3.4,
            48.5, 4.22, 18.6, 15, 184, 35, 17, 88, 19
            ]
start_num = int(input("Введите число начала диапазона: "))
stop_num = int(input("Введите число конца диапазона (не включая): "))
print(count_range(num_list, start_num, stop_num))

# Ex_8 Количество подсписков
count_list = []


def list_(lst):
    for i in lst:
        if isinstance(i, list):
            list_(i)
            count_list.append(1)
        else:
            pass
    return len(count_list)


my_list = [1, [2, 3], [4, [5, [6, [152, 12, [15, 15, 2.022, [1523, 1524]]], 7]]], [[[8], 9], [10]]]
print(list_(my_list))


# Ex_9 Анаграммы, работает, но на разных словах не проверял
def anagram(word_1, word_2):
    count = 0
    for i in word_1:
        if i in word_2:
            count += 1
    if count == len(word_2):
        return f"Слова {word_1} и {word_2} являются анаграммами"
    else:
        return "Введенные слова не авляются анаграммами"


input_word_1 = input("Введите слово 1: ")
input_word_2 = input("Введите слово 2: ")
print(anagram(input_word_1, input_word_2))


# Ex_10 Клавиатура старого телефона
def opk(str_):
    old_phone_keyboard = {".": 1, ",": 11, "?": 111, "!": 1111, ":": 11111,
                          "a": 2, "b": 22, "c": 222,
                          "d": 3, "e": 33, "f": 333,
                          "g": 4, "h": 44, "i": 444,
                          "j": 5, "k": 55, "l": 555,
                          "m": 6, "n": 66, "o": 666,
                          "p": 7, "q": 77, "r": 777, "s": 7777,
                          "t": 8, "u": 88, "v": 888,
                          "w": 9, "x": 99, "y": 999, "z": 9999,
                          " ": 0
                          }
    print("\nПоследовательность нажатий кнопок для ввода текста на старом телефоне: ")
    for i in str_.lower():
        print(old_phone_keyboard.get(i), end=" ")


opk(input("Введите текст: "))

# Ex_11
flat_list = []


def list_flattering(lst):
    for i in lst:
        if isinstance(i, list):
            list_flattering(i)
        else:
            flat_list.append(i)
    return flat_list


my_list = [1, [2, 3], [4, [5, [6, [152, 12, [15, 15, 2.022, [1523, 1524]]], 7]]], [[[8], 9], [10]]]
print()
print(list_flattering(my_list))
