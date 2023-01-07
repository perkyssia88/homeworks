# Ex 5
string = input("Enter some string: ")  # просим ввести текст(str)
# Выводим на экран срез от пробела до конца строки
# +1 - чтобы убрать тот самый пробел, иначе он будет передпервым словом
# второй строкой выводим первое слово
print(string[string.find(" ") + 1:], string[:string.find(" ")])

# Homework Ex 1
my_string = input("Enter some text: ")  # просим ввести текст(str)
print(my_string[2])  # третий символ
print(my_string[-2])  # второй с конца
print(my_string[:5])  # от начала до пятого символа
print(my_string[:-2])  # от начала до предпоследного
print(my_string[::2])  # все четные
print(my_string[1::2])  # все нечетные
print(my_string[::-1])  # строка в обратном порядке
print(my_string[::-2])  # строка в обратном порядке через 1 символ
print(len(my_string))  # количество строк
