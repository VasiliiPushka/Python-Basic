import random
class People:
    def __init__(self, name, home, satiety=50):
        self.name = name
        self.satiety = satiety
        self.home = home
    def print_info(self):
        print(f'Имя: {self.name}\nСытость :{self.satiety}')
    def eat(self):
        self.home.food -= 20
        self.satiety += 10
        print(f'{self.name} поел\n')
    def work(self):
        self.satiety -= 10
        self.home.money += 50
        print(f'{self.name} ушел на работу!')
    def play(self):
        self.satiety -= 10
        print(f'{self.name} играет.')
    def go_for_food(self):
        self.home.food += 20
        self.home.money -= 20
        print(f'{self.name} пошел в магазин!\n')

    def live_one_day(self):
        choice = random.randint(1, 6)
        if self.satiety < 20:
            print(f'{self.name}, надо поесть!\n')
            self.eat()
        elif self.home.food < 10:
            self.go_for_food()
        elif self.home.money < 50:
            self.work()
        elif choice == 1:
            self.work()
        elif choice == 2:
            self.eat()
        else:
            self.play()
class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money
    def print_info(self):
        print(f'Еды в холодильнике: {self.food}\nденег в тумбочке: {self.money}')


apartment = House()
man = People('Михаил', apartment)
man_2 = People('Алина', apartment)

day = 1
while day != 365:
    day += 1
    man.live_one_day()
    man_2.live_one_day()
    if man.satiety < 0 or man_2.satiety < 0:
        if man.satiety < 0:
            print(f'{man.name} умер :(')
        else:
            print(f'{man_2.name} умер :(')
        break
print(man.satiety, day)
print(man_2.satiety, day)















