class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        name = args[0]
        cls.houses_history.append(name)
        print(cls.houses_history)
        return super().__new__(cls)

    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


    # def go_to(self, new_floor):
    #     if new_floor < 1 or new_floor > self.number_of_floors:
    #         print('Такого этажа не существует')
    #     else:
    #         for new_floor in range(1, new_floor + 1):
    #             print(f'этаж {new_floor}')

    # def __len__(self):
    #     return self.number_of_floors
    #
    # def __str__(self):
    #     return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
    #
    # def __eq__(self, other):
    #     return self.number_of_floors == other.number_of_floors
    #
    # def __lt__(self, other):
    #     return self.number_of_floors < other.number_of_floors
    #
    # def __le__(self, other):
    #     return self.number_of_floors <= other.number_of_floors
    #
    # def __gt__(self, other):
    #     return self.number_of_floors > other.number_of_floors
    #
    # def __ge__(self, other):
    #     return self.number_of_floors >= other.number_of_floors
    #
    # def __ne__(self, other):
    #     return self.number_of_floors != other.number_of_floors
    #
    # def __add__(self, value):
    #     self.number_of_floors += value
    #     return self
    #
    # def __iadd__(self, other):
    #     return self + other
    #
    # def __radd__(self, other):
    #     return self + other


h1 = House('"ЖК Горский"', 10)
h2 = House('"Домик в деревне"', 20)
h3 = House('"ЖК МАТРЁШКИ"', 20)

del h2
del h3
print(House.houses_history)
# h1.go_to(5)
# h2.go_to(10)
# print(len(h1))
# print(len(h2))
# print(h1)
# print(h2)
# print(h1 == h2)
# h1 = h1 + 10
# print(h1)
# print(h1 == h2)
# h1 += 10
# print(h1)
# h2 = h2 + 10
# print(h2)
# print(h1 > h2)
# print(h1 >= h2)
# print(h1 < h2)
# print(h1 <= h2)
# print(h1 != h2)


