import random
class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.force = 20
    def helth_point(self):
        print('Health {}: {}'.format(self.name, self.health))
    def strike_warrior(self):
        print('the {} warrior strikes!'.format(self.name))
    def winner(self):
        print('\nWinner: {}'.format(self.name))

user_1 = Warrior('War1')
user_2 = Warrior('War2')
while user_1.health != 0 and user_2.health != 0:
    num = random.randint(1, 2)
    if num == 1:
        user_1.strike_warrior()
        user_2.health -= 20
        user_2.helth_point()
    elif num == 2:
        user_2.strike_warrior()
        user_1.health -= 20
        user_1.helth_point()
if user_1.health > 0:
    user_1.winner()
else:
    user_2.winner()





