@staticmethod
def num_sum(a):
    count = a % 10 + a // 10
    return print(f"Число {a} четное, "
                 f"сумма его цифер равна {count}")


@staticmethod
def vowel_consonant():
    vow_leters = "aeiuyo"
    vow_total = 0
    cons_total = 0
    for _ in i:
        if _ in vow_leters:
            vow_total += 1
        else:
            cons_total += 1
    return print(f"В слове {i} {vow_total} гласных(ая) и "
                 f"{cons_total} согласных(ая) букв")


lst = [15, 48, "hello", 6, 19, "world"]
print(f"Список до начала работы с ним - {lst}")
for i in lst:
    if type(i) is int:
        if i % 2 == 0:
            num_sum(i)
        else:
            print(f"Число {i} нечетное, "
                  f"заменяем его в списке на 1")
            lst[lst.index(i)] = 1
        pass
    elif type(i) is str:
        vowel_consonant()
print(f"Список после работы с ним - {lst}")
