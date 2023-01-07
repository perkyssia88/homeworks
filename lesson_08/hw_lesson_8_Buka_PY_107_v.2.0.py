# Ex_2
lst = [15, 48, "hello", 6, 19, "world"]
print(f"Список до начала работы с ним - {lst}")
for i in lst:
    if type(i) == int:
        if i % 2 == 0:
            count = i % 10 + i // 10
            print(f"Число {i} четное, "
                  f"сумма его цифр равна {count}")
        else:
            print(f"Число {i} нечетное, "
                  f"заменяем его в list на 1")
            lst[lst.index(i)] = 1
    elif type(i) == str:
        vow_leters = ["a", "e", "i", "u", "y", "o"]
        vow_total = 0
        cons_total = 0
        for j in i:
            if j in vow_leters:
                vow_total += 1
            else:
                cons_total += 1
        print(f"В слове {i} {vow_total} гласных(ая) и "
              f"{cons_total} согласных(ая) букв")
print(f"Список после работы с ним - {lst}")
