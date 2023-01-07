# # Practice Ex_1
# def div(a, b):
#     try:
#         a / b
#         return (a / b) ** 2
#     except ZeroDivisionError:
#         return "На ноль делить нельзя!"
#     finally:
#         print("Функция завершила работу")
#
#
# n1, n2 = int(input()), int(input())
# print(div(n1, n2))
#
# # Practice Ex_2
# def div2(a, b):
#     try:
#         res = int(a) / int(b)
#         return res
#     except ZeroDivisionError:
#         return "На ноль делить нельзя!"
#     except ValueError:
#         return "Неверный тип данных"
#     except Exception:
#         return "Какая-то другая ошибка произошла," \
#                " общее исключение сработало"
#
#
# num1, num2 = input(), input()
# print(div2(num1, num2))
