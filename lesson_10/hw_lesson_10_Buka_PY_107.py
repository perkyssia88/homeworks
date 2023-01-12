from random import randint  # for Ex_1 and Ex_3

# Ex_1
# создаем список из 20 случайных цифр от 0 до 9
tup_list = [randint(0, 9) for _ in range(20)]
# преобразуем список в кортеж
tuple_1 = tuple(tup_list)
# выводим на печать кортеж
print(tuple_1)
# выводим на печать сумму цифр кортежа
print(sum(tuple_1))

# Ex_2
# переменная кортеж
long_word = ("т", "т", "а", "и", "и", "а", "и",
             "и", "и", "т", "т", "а", "и", "и",
             "и", "и", "и", "т", "и")
# пустой список для исключения повторений
# вывода на экран одной и той же буквы
letter = []
# итертируемся по кортежу
for i in long_word:
    # если объект из котрежа есть в списке
    if i in letter:
        # ничего не делаем
        pass
    # если его в списке нет
    else:
        # добавляем его в конец списка
        letter.append(i)
        # считаем количество вхождений в котреж
        count = long_word.count(i)
        # выводим на экран объект и кол-во его вхождений
        # считаем % соотношение вхождений объекта и кол-ва всех объектов в кортеже
        print(f"В кортеже long_world объект \"{i}\" встречается {count} раз(а) "
              f"из {len(long_word)} объектов, а это "
              f"{round(count / len(long_word) * 100, 2)} % от общего количества.")

# Ex_3
# заполняем кортеж через генератор случайных чисел
week_temp = tuple(
    [randint(12, 32) for i in range(int(input("Введите количество дней: ")))]
)
# # или через пользовательский ввод
# week_temp = tuple(
#     [float(input("Введите температуру: "))
#      for i in range(int(input("Введите количество дней: ")))]
# )
# считем сумму объектов кортежа
sum_temp = sum(week_temp)
# узнаем количество объектов кортежа
days = len(week_temp)
# вычисляем среднюю температуру
mean_temp = sum_temp / days
# выводим на экран количество дней и сред. темп. округленную до 1 знака после точки
print(f"Средняя температура за {days} дней(день) равна {round(mean_temp, 1)} градуса")