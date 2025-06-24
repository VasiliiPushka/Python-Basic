import random

class Unit:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.force = 20

    def health_point(self):
        return f'{self.name} - {self.health}'

    def strike(self):
        print(f'{self.name} наносит удар')

    def damage(self):
        self.health -= 20
        print(f'{self.name} получил урон')

    def winner(self):
        print(f'{self.name} одержал победу!')




unit_1 = Unit('warrior_1')
unit_2 = Unit('warrior_2')

while unit_1.health > 0 and unit_2.health > 0:
    choice = random.randint(1, 2)

    if choice == 1:
        unit_1.strike()
        unit_2.damage()
        print(f'{unit_1.health_point()} | {unit_2.health_point()}\n')

    if choice == 2:
        unit_2.strike()
        unit_1.damage()
        print(f'{unit_1.health_point()} | {unit_2.health_point()}\n')

if unit_1.health > 0:
    unit_1.winner()
else:
    unit_2.winner()











