from math import *
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        super().area()
        area = pi * self.radius ** 2
        return area.__round__(2)

class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
    def area(self):
        super().area()
        area = self.side_a * self.side_b
        return area.__round__(2)    

class Triangle(Shape):
    def __init__(self, side_a, height):
        super().__init__()
        self.side_a = side_a
        self.height = height
    def area(self):
        super().area()
        area = (self.side_a * 0.5) * self.height
        return area.__round__(2)

# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)

