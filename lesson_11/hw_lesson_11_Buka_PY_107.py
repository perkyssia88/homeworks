from random import randint  # for Ex_6


# Ex_2 Високосный год
def is_year_leap(a):
    return a % 4 == 0 and a % 100 != 0 or a % 400 == 0


year = int(input("Введите год: "))
print(is_year_leap(year))


# Ex_3 Периметр, площадь и диагональ квадрата по стороне
def calc_quadrate(a):
    perimeter = a * 4
    square = a ** 2
    diagonal = 2 ** 0.5 * a
    return (perimeter, square, diagonal)


leg = int(input("Введите сторону квадрата: "))
print(calc_quadrate(leg))


# Ex_4 Времена года по введенному месяцу
def season(a):
    if 1 <= a <= 12:
        match a:
            case 1 | 2 | 12:
                return "Winter"
            case 3 | 4 | 5:
                return "Spring"
            case 6 | 7 | 8:
                return "Summer"
            case _:
                return "Autumn"
    else:
        return "Неверный номер месяца"


month_input = int(input("Введите номер месяца: "))
print(season(month_input))


# Ex_5 Простое ли число
def is_prime(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True


num_input = int(input("Введите целое число: "))
print(is_prime(num_input))


# Ex_6 Среднее арифметическое списка (случайных) чисел
def average(a):
    return sum(a) / len(a)


lst = [randint(1, 10000) for _ in range(10)]
print(average(lst))


# Homework Калькулятор
def give_sum(a=1, b=0):
    return a + b


def give_minus(a=2, b=1):
    return a - b


def give_mul(a=1, b=1):
    return a * b


def give_div(a=1, b=1):
    try:
        return a / b
    except ZeroDivisionError:
        return "На ноль делить нельзя!"


while True:
    num1 = input("Введите число 1: ")
    num2 = input("Введите число 2: ")
    sign = input("Введите оператор (+, -, *, / или 'n' для выхода: ")
    if num1.isdigit() and num2.isdigit():
        num1 = float(num1)
        num2 = float(num2)
        match sign:
            case "+":
                print(give_sum(num1, num2))
            case "-":
                print(give_minus(num1, num2))
            case "*":
                print(give_mul(num1, num2))
            case "/":
                print(give_div(num1, num2))
            case "n":
                print("Выполнение программы завершено")
                break
            case _:
                print("Неверный знак оператора")
    else:
        print("Вы ввели не числовые значения")
