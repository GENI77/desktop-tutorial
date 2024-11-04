import math

class Figure:
    sides_count = 0

    def __init__(self, color: list[int, int, int], *sides):
        if self.__is_valid_color(color[0], color[1], color[2]):
            self._color = list(color)
        else:
            print("Invalid color", color)
        self._sides = sides
        self.filled = False

    def get_color(self):
        return self._color


    def __is_valid_color(self, r, g, b):
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_types and valid_values


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *sides):
        if len(sides) == len(self._sides):
            valid_sides = []
            for side in sides:
                if self.__is_valid_sides(side):
                    valid_sides.append(side)
            self._sides = valid_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, count):
        super().__init__(color, count)
        self.__radius = count / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, a, b, c, P):
        Figure.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.P = P

    def Perimeter(self):
        self.Perimeter()
        self.P = self.a + self.b + self.c
        return self.P


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge):
        sides = [edge] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        edge = self.get_sides()[0]
        return edge ** 3






circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)# Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

