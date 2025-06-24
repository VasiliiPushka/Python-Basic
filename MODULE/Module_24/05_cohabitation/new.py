import random

def logic_life(people):
    number = random.randint(1, 6)
    if people.fullness < 20:
        people.eating()
    elif people.home.refrigerator < 10:
        people.market()
    elif people.home.bank < 50:
        people.working()
    elif number == 1:
        people.working()
    elif number == 2:
        people.eating()



class People:

    def __init__(self, name:str, home, fullness=50):
        self.name = name
        self.fullness = fullness
        self.home = home


    def eating(self):
        self.fullness += 10
        self.home.refrigerator -= 10
        print(f"{self.name} - поел")

    def working(self):
        self.fullness -= 10
        self.home.bank += 20
        print(f"{self.name} пошел на работу")

    def playing(self):
        self.fullness -= 10
        print(f'{self.name} поиграл и поел')

    def market(self):
        self.home.refrigerator += 10
        self.home.bank -= 10
        print(f"{self.name} сходил(а) в магазин."
              f"Еды в доме - {self.home.refrigerator} | денег в тумбочке - {self.home.bank}")

    def info(self):
        print(f"имя - {self.name} | сытость - {self.fullness}")


class Home:

    def __init__(self, refrigerator=50, bank=0):
        self.refrigerator = refrigerator
        self.bank = bank

    def info(self):
        print(f"еды в холодильнике осталось - {self.refrigerator} | "
              f"денег в тумбочке - {self.bank}")


days = 365

home = Home()
people_1 = People(name='Артем', home=home)
people_2 = People(name='Женя', home=home)

peoples = [people_1, people_2]

while days > 0:
    days -= 1
    for person in peoples:
        logic_life(person)
        if person.fullness <= 0:
            print(f'{person.name} - умер')
            break
    else:
        continue
    break












