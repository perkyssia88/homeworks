# Ex_1
with open("example.txt", encoding="utf-8") as e:
    string = e.readline().split(" ")
    print(string)
    sum_ = 0
    for i in string:
        try:
            int(i)
            sum_ += int(i)
        except:
            pass
print(sum_)

# Ex_2
with open("tester.txt", encoding="utf-8") as t:
    num_lst = []
    str_lst = []
    for i in t.readlines():
        try:
            str_lst.append(i.replace("\n", ""))
        except:
            pass
    for i in str_lst:
        try:
            isinstance(int(i), int)
            num_lst.append(int(i))
            str_lst.remove(i)
        except:
            pass
    print(sorted(num_lst) + sorted(str_lst, key=len))

# Ex_3
with open("test.txt", "w", encoding="utf-8") as t:
    while True:
        s = input("Введите какой-либо текст, для выхода нажмите Enter без ввода текста: ")
        if s == "":
            break
        else:
            t.write(s + "\n")

# Ex_4
with open("test_2.txt", encoding="utf-8") as t:
    count_lines = 0
    for i in t.readlines():
        count_lines += 1
        count_symbols = 0
        for j in i.replace("\n", ""):
            count_symbols += 1
        print(f"Количество символов в строке {count_lines} равно {count_symbols}")
    print(f"Количество строк в файле - {count_lines}")

# Homework
"""
Есть массив состоящий из слов и чисел, нужно записать в файл сначала слова
в порядке их длины, а после слов цифры в порядке возрастсния
"""
lst = [12, 45, "hello", 78, "Hi", "Privet", 23, 56,
       "Python", 89, 13, "world", 64, "No", 97]

num_lst = []
str_lst = []

for i in lst:
    if isinstance(i, int):
        num_lst.append(i)
    else:
        str_lst.append(i)

with open("homework.txt", "w+", encoding="utf-8") as hw:
    for _ in sorted(str_lst, key=len):
        hw.write(_ + " ")   # через пробел в одну строку
    hw.write("\n")
    for _ in sorted(num_lst):
        hw.write(str(_) + " ")