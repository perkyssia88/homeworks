# Ex 7 (Найти площадь и периметр прямоугольного треугольника)
from math import sqrt  # импортируем из модуля math функцию sqrt

# закрашиваем у пользователя длинну катета № 1
# преобразуем из str во float
leg_1 = float(input("Введите длину катета №1: "))
# закрашиваем у пользователя длинну катета № 2
# преобразуем из str во float
leg_2 = float(input("Введите длину катета №2: "))
s = 0.5 * leg_1 * leg_2  # вычисляем по формуле площадь
# вычисляем по формуле периметр
p = sqrt(leg_1 ** 2 + leg_2 ** 2) + leg_1 + leg_2
# выводим на экран результат
print(f"Площадь прямоугольного треугольника равна: {s}")
# выводим на экран результат
print(f"Периметр прямоугольного треугольника равен: {p}\n")

# creative task
# В купейном вагоне имеется 9 купе
# с четырьмя местами для пассажиров в каждом.
# Напишите программу, которая определяет номер купе, в котором
# находится место с заданным номером
# нумерация мест сквозная, начинается с 1.

# просим пользователя ввести номер своего места
# переводим из str в int
seat_num = int(input("Введите номер места: "))
# рассчитываем исходя из номера места номер купе
coupe_num = (seat_num + 3) // 4
# выводим на печить номер купе
print(f"Ваше место в купе номер {coupe_num}, приятной поездки\n")
# ждем нажатия enter для продолжения выполнения программы
print(input("Нажмите Enter чтобы продолжить"))

# Homework Ex 1
anna_apple = 2  # кол-во яблок у Анны
paul_apple = 5  # кол-во яблок у Пола
# выводим количество яблок у обоих в одну строку
print(f"У Анны {anna_apple} яблока, а у Пола {paul_apple} яблок")
# можно вывести вот таким форматом
print("У Анны", anna_apple, "яблока, а у Пола", paul_apple, "яблок")
print("У Анны " + str(anna_apple) + " яблока, а у Пола "
      + str(paul_apple) + " яблок\n")  # или в таком

# Homework Ex 2
# Просим ввести длину ребра куба и переводим из str во float
face_cube = float(input("Введите длинну ребра куба: "))
# вычисляем объем куба
v_cube = face_cube ** 3
# вычисляем площадь боковой поверхности
p_cube = 4 * face_cube ** 2
print(f"Объем куба составит: {v_cube}. "
# выводим на экран результат
      f"Площадь боковой поверхности: {p_cube}\n")
# ждем нажатия enter для продолжения выполнения программы
print(input("Нажмите Enter чтобы продолжить"))

# Homework Ex 3 немного скучно, решил через условный цикл
tree_height = 20  # высота дерева
move_up = 2  # движение вверх
move_down = 1  # сползание вниз
travel_days = 0  # счетчик количества дней на пути к вершине дерева
# пока не залезем наверх будет выполняться тело цикла
while tree_height != 1:
# отнимаем от высоты дерева пройденое растояние вверх и прибавляем
# сползание вниз(!важно чтобы улитка ползла вверх!)
    tree_height = tree_height - move_up + move_down  # замкнутого цикла нет
    travel_days += 1  # прибавляем к счетчику один день
# выводим общее количество дней для достижения вершины дерева
print(f"Улитке ползти до вершины дерева {travel_days} дней")
