# создаем класс
class Human:
    # создаем два статических поля
    default_name = "Ivan"
    default_age = 33

    # создаем инициализатор с 4 динамическими полями
    # и 2 параметрами со значениями по умолчанию из статических полей
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 1000
        self.__house = "Дома нет"

    # создаем метод для получения информации из динамических полей
    def info(self):
        print(f"Имя - {self.name}")
        print(f"Возраст - {self.age}")
        print(f"Дом - {self.__house}")
        print(f"Деньги - {self.__money}")

    # создаем статический метод для получения информации из статических полей
    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    # создаем метод для изменения динамической приватной переменной(поля)
    def earn_money(self, arg):
        self.__money += arg

    # создаем метод для изменения динамических приватных переменных(полей)
    # из __money отнимаем значение параметра price
    # __house присваиваем значение параметра house
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    # создаем метод с двумя параметрами
    def buy_house(self, house, discount):
        # создаем переменную цены дома
        # присваиваем ей значение экземпляра класса SmallHouse из параметра метода
        # с методом final_price и аргументом из параметра метода buy_house
        price = house.final_price(discount)
        # если денег больше или равно цене дома
        if self.__money >= price:
            # выполняем приватный метод по покупке дома,
            # в качестве аргументов передаем экземпляр класса SmallHouse и локальную переменную price
            self.__make_deal(house, price)
            print("Дом куплен")
        else:
            print("Не хватает денег для покупки")


# создаем класс
class House:

    # создаем инициализатор с 2-мя параметрами
    # и 2-мя динамическими полями, полям присваиваем значения параметров
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (100 - discount) / 100


# создаем класс и наследуем от родительского класса House все методы и свойства
class SmallHouse(House):
    # создаем статическое поле класса
    default_area = 40

    # в инициализаторе с помощью метода super обращаемся к родительскому классу
    # и перегружаем(переопределяем) параметры его метода __init__
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


# Вызаваем статический метод класса Human
Human.default_info()
print()
# создаем экземпляр(объект) класса Human
person = Human("Valera", 50)
# к экземпляру класса применяем метод экземпляра класса(посмотреть информацию)
person.info()
print()
# к экземпляру класса применяем метод экземпляра класса(добавляем денег)
person.earn_money(1500)
person.info()
print()
# создаем экземпляр класса SmallHouse
s_h = SmallHouse(5000)
# к экземпляру класса применяем метод экземпляра класса(пытаемся купить дом)(не получится)
person.buy_house(s_h, 1)
print()
# к экземпляру класса применяем метод экземпляра класса(добавляем денег)
person.earn_money(3000)
# к экземпляру класса применяем метод экземпляра класса(пытаемся купить дом еще раз)(успешно)
person.buy_house(s_h, 1)
print()
# к экземпляру класса применяем метод экземпляра класса(посмотреть информацию)
person.info()
