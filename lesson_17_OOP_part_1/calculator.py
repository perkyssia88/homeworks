# Создаем класс
class Calculator:
    # здесь могут быть статические поля (свойства, переменные, атрибуты) класса

    # объект созданный маг. методом __new__ затем передается в инициализатор
    def __init__(self):
        # динамические поля (свойста, переменные, атрибуты) класса
        self.user_input()

    # Создаем методы экземпляра класса(отдельно для *, /, **, +, и -)
    def sum_(self):
        # self - ссылка на текущий экземпляр(объект) класса
        self.s = self.num_1 + self.num_2
        return f"Сумма {self.num_1} и {self.num_2} равна {self.s}"

    def minus_(self):
        self.m = self.num_1 - self.num_2
        return f"Разность {self.num_1} и {self.num_2} равна {self.m}"

    def mul_(self):
        self.mul = self.num_1 * self.num_2
        return f"Произведение {self.num_1} и {self.num_2} равно {self.mul}"

    def power_(self):
        self.power = self.num_1 ** self.num_2
        return f"Число {self.num_1} в степени {self.num_2} равно {self.power}"

    # Неверно работает исключение, пересмотреть
    # пересмотрел через 2 дня и все работает, либо чудеса, либо нельзя писать код в час ночи
    def div_(self):
        try:
            self.div = self.num_1 / self.num_2
        except ZeroDivisionError:
            return "На ноль делить нельзя!"
        else:
            return f"Частное чисел {self.num_1} и {self.num_2} равно {self.div}"

    def user_input(self):
        while True:
            try:
                self.num_1 = int(input("Введите число 1: "))
                self.num_2 = int(input("Введите число 2: "))
                break
            except ValueError:
                print("Неверный формат ввода, введите числа повторно")


# блок запроса математического знака
def sign_():
    """
    :return: mathematical symbol entered by the user (+, -, /, * or **)
    """
    signs = ["+", "-", "/", "*", "**"]
    sign = input("Введите знак действия (+, -, *, / или **): ")
    if sign not in signs:
        print("Данный вид вычислений не поддерживается!")
        return sign_()
    else:
        return sign


# блок вычислений и вывода результатов
while True:
    stop_sign = input("Введите - чтобы выйти из программы или Enter чтобы продолжить: ")
    if stop_sign == "-":
        print("Программа завершена")
        break
    else:
        # Создаем объект(экземпляр) класса Calculator
        calc = Calculator()
        match sign_():
            case "+":
                print(calc.sum_())
            case "-":
                print(calc.minus_())
            case "/":
                print(calc.div_())
            case "*":
                print(calc.mul_())
            case "**":
                print(calc.power_())
    print()
print()
