"""Два метода в классе, один принимает в себя либо строку, либо число.+
Если передаем строку, то:+
если произведение гласных и согласных букв меньше или равно длине слова+
- выводить все гласные, иначе - согласные.+
если число - выводим произведение суммы четных цифр на длину числа.
Длину строки и числа искать во втором методе.
"""


class Example:

    def __init__(self):
        self.user_input = input("Введите строку на русском языке или число: ")

    def method_1(self):
        try:
            self.num = int(self.user_input)
        # если переданный объект - не число(строка)
        except ValueError:
            self.vowels = "ауоиэыяюеё"
            self.vow_count = []
            self.cons_count = []
            for i in self.user_input.lower():
                if i in self.vowels:
                    self.vow_count.append(i)
                else:
                    self.cons_count.append(i)
            # если произведение гласных и согласных меньше или равно длине слова
            # длину слова берем из method_2
            if len(self.vow_count) * len(self.cons_count) <= self.method_2():
                # выводим гласные
                return self.vow_count
            else:
                # иначе согласные
                return self.cons_count
        else:
            # сумма четных цифр
            self.even_nums = 0
            for i in str(self.num):
                if int(i) % 2 == 0:
                    self.even_nums += int(i)
            # произведение суммы четных цифр на длину числа
            return self.even_nums * self.method_2()

    def method_2(self):
        # по сути неважно что мы вводим число или строку, в input будет строковое значение
        self.len_ = len(self.user_input)
        return self.len_


# создаем экземпляр класса Example
s = Example()
print(f"Итог работы метода s.method_1 - {s.method_1()}")
print(f"Итог работы метода s.method_2 - {s.method_2()}")