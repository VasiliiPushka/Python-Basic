import math


class MyMath(math):

    def __init__(self, radius: int, length: int) -> None:
        self.radius = radius
        self.length = length

    @classmethod
    def len_circle(cls, radius: int) -> float:
        len_circe = math.pi * radius * 2
        return len_circe

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        circle_sq = math.pi * radius ** 2
        return circle_sq

    @classmethod
    def volume_qube(cls, length: int) -> int:
        volume_qube = length ** 3
        return volume_qube

    @classmethod
    def square_sphere(cls, radius: int) -> float:
        square_sphere = 4 * math.pi * radius ** 2
        return square_sphere


res_1 = MyMath.len_circle(5)
print(res_1)
res_2 = MyMath.circle_sq(radius=6)
print(res_2)
res_3 = MyMath.volume_qube(length=4)
print(res_3)
res_4 = MyMath.square_sphere(radius=13)
print(res_4)
