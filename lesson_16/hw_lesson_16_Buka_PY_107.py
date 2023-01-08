# Practice Ex_1
def div(a, b):
    try:
        a / b
        return (a / b) ** 2
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    finally:
        print("Функция завершила работу")


n1, n2 = int(input("Число 1: ")), int(input("Число 2: "))
print(div(n1, n2))


# Practice Ex_2
def div2(a, b):
    try:
        res = int(a) / int(b)
        return res
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    except ValueError:
        return "Неверный тип данных"
    except Exception:
        return "Какая-то другая ошибка произошла," \
               " общее исключение сработало"


num1, num2 = input("Ввод 1: "), input("Ввод 2: ")
print(div2(num1, num2))

""" Homework
Ввод с клавиатуры. Если строка введенная с клавиатуры - числа, то поделить первое на второе.
Обработать ошибку деления на ноль. Если второе число 0, то запросить ввод заново.
Если введены буквы, то обработать исключение.
"""


def div_input_nums():
    """
    :return: asking for user input, str[0]/str[1],
    handled exceptions ZeroDivisionError & ValueError
    """
    user_input = input("Введите строку из 2-х чисел раздеделенных пробелом: ")
    lst = user_input.split(" ")
    try:
        div = int(lst[0]) / int(lst[1])
    except ValueError:
        return div_input_nums()
    except ZeroDivisionError:
        return div_input_nums()
    except IndexError:
        return div_input_nums()
    else:
        return f"Частное введенных чисел равно: {div}"


print(div_input_nums())
