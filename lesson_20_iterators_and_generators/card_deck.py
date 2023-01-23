"""
Реализуйте итератор колоды карт (52 штуки) CardDeck.
Каждая карта представлена в виде строки типа "2 Пик".
При вызове функции next() будет представлена следующая карта.
По окончании перебора всех элементов возникнет ошибка StopIteration
"""


class CardDeck:
    def __init__(self):
        self.num_of_cards = 52
        self.start = 0
        self.suit = ["червы", "бубны", "трефы", "пики"]
        self.value = [2, 3, 4, 5, 6, 7, 8, 9, 10,
                      "валет", "дама", "король", "туз"]

    def __next__(self):
        if self.start >= self.num_of_cards:
            raise StopIteration
        else:
            rank = self.value[self.start % len(self.value)]
            suit = self.suit[self.start // len(self.value)]
            self.start += 1
            return f'{rank} {suit}'

    def __iter__(self):
        return self


deck = CardDeck()
while True:
    print(next(deck))
