"""
Напишите декоратор debug, который при каждом вызове декорируемой функции выводит ее имя
(вместе со всеми передаваемыми аргументами), а затем - какое значение она возвращает.
После этого выводится результат ее выполнения.
"""


def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Имя декорируемой функции - {func.__name__}")
        print(f"Позиционные аргументы декорируемой функции - {args}")
        print(f"Ключевые аргументы декорируемой функции - {kwargs}")
        result = func(*args, **kwargs)
        print(f"Декорируемая функция возвращает значение - {result}")
        print(result)
        return result

    return wrapper


@debug
def example(*args, **kwargs):
    lst = [_ for _ in args if _ % 2 == 1]
    string_list = []
    for value in kwargs.values():
        if isinstance(value, str) and value.isalpha():
            for letter in value:
                string_list.append(letter)
    return sum(lst) + len(string_list)


example(15, 20, 12, 13, 1984, 2055, 255, 1, name="Ivan", age=33, email="ivan@gmail.ca")     # 2339 + 4
