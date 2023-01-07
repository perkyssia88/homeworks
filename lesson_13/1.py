# # Ex_2
# with open("tester.txt", encoding="utf-8") as t:
#     num_lst = []
#     str_lst = []
#     for i in t.readlines():
#         try:
#             str_lst.append(i.replace("\n", ""))
#         except:
#             pass
#     for i in str_lst:
#         try:
#             isinstance(int(i), int)
#             num_lst.append(int(i))
#             str_lst.remove(i)
#         except:
#             pass
#     print(sorted(num_lst) + sorted(str_lst, key=len))

with open("tester.txt", encoding="utf-8") as te:
    str_ = te.readlines()
    num_list = []
    str_list = []
    for i in str_:
        if '\n' in i:
            i = i[:-1]
        if i.isdigit():
            num_list.append(int(i))
        else:
            str_list.append(i)
print(num_list)
print(str_list)

f = open("tester.txt")
b = []
n = []
s = f.readlines()
print(s)
for i in s:
    if "\n" in i:
        i = i[:-1]
    if i.isalpha():
        i = str(i)
        b.append(i)
    elif i.isdigit():
        i = int(i)
        n.append(i)
print(b)
print(n)
n.sort(key=len)
b.sort()
mas = n + b
print(mas)