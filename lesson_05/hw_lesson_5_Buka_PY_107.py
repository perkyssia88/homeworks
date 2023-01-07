# ex_1
i = 1
while i <= 10:
    print(f"Квадрат числа {i} равен {i ** 2}")
    i += 1

# ex_2
i = 1
total = 0
while i < 125:
    if i % 2 == 0:
        total = i * i
        print(total)
    i += 1

# ex_3
i = 15
while i != 0:
    print(i)
    i -= 1

# ex_4
user_num = int(input("Введите целое число: "))
user_num_2 = int(input("Введите второе целое число: "))
if user_num < 0 and user_num < user_num_2:
    while user_num <= user_num_2:
        print(user_num)
        user_num += 1
        if user_num == 0:
            break
elif user_num_2 < 0 and user_num_2 < user_num:
    while user_num_2 <= user_num:
        print(user_num_2)
        user_num_2 += 1
        if user_num_2 == 0:
            break
elif user_num == user_num_2 and user_num < 0:
    print(user_num)
else:
    print("Отрицательных чисел нет")
