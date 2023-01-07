from json import dump, load

products = {}
while True:
    user_input = input("Введите покупку(для завершения введите \"стоп\"): ")
    user_input2 = input("Введите стоимость покупки: ")
    if user_input.lower() == "стоп":
        break
    else:
        products.setdefault(user_input, user_input2)
with open("data.json", "w", encoding="utf-8") as data:
    dump(products, data, ensure_ascii=False)

with open("data.json", encoding="utf-8") as data:
    j_load = load(data)
    cost = 0
    print(j_load)
    for i in j_load.values():
        cost += int(i)
# print(cost)