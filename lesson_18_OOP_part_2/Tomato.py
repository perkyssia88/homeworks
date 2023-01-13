class Tomato:
    states = {1: "саженец", 2: "цветение",
              3: "созревание", 4: "зрелый помидор"
              }

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        self._state += 1

    def is_ripe(self):
        if self._state == 4:
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, tomato_num):
        self.tomatoes = []
        for i in range(tomato_num):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        false_count = 0
        for i in self.tomatoes:
            if not i.is_ripe():
                false_count += 1
        if false_count == 0:
            return True
        else:
            return False

    def give_away_all(self):
        self.tomatoes.clear()
        # print(f"{self.tomatoes}")   # проверить очистился ли список


class Gardener:

    def __init__(self, name, plant):
        self.__name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        print(f"{self.__name} поработал")

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Помидоры созрели, урожай собран")
        else:
            print("Не все помидоры созрели")

    @staticmethod
    def knowledge_base():
        print("Какая-то справка по садоводсту...")


Gardener.knowledge_base()
bush = TomatoBush(1)
gardner = Gardener("Ivan", bush)
gardner.work()
gardner.harvest()
gardner.work()
gardner.harvest()
gardner.work()
gardner.harvest()
