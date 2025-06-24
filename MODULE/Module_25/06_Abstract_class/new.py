import math
from abc import abstractmethod, ABC



class Shape(ABC):

    @abstractmethod
    def __init__(self) -> float:
        pass

    @abstractmethod
    def area(self) -> str:
        pass


class Circle(Shape):

    def __init__(self, radius:float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Площадь круга = {str(self.area())}"


class Rectangle(Shape):

    def __init__(self, side_a: float, side_b: float):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны должны быть положительными")
        self.side_a = side_a
        self.side_b = side_b

    def area(self) -> float:
        return self.side_a * self.side_b


class Triangle(Shape):

    def __init__(self, base: float, height: float):
        if base <= 0 or height <= 0:
            raise ValueError("Основание и высота должны быть положительными")
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height