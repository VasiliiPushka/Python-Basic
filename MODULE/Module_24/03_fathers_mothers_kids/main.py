import random

class Parent:
    list_child = []
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def print_info(self):
        print('Имя: {}\nВозраст: {}\nСписок детей: {}'.format(
            self.name, self.age, self.list_child)
        )


    def feed_child(self):
        print('ребенок поел\n')


    def calm_dawn(self):
        print('ребенок успокоился\n')


class Child:

    def __init__(self, name, age, hungry, calmness):
        self.hungry = hungry
        self.calmness = calmness
        self.name = name
        self.age = age

    def state_of_hunger(self):
        if self.hungry == True:
            print('{} хочет кушать\n'.format(self.name))
        else:
            print('{} не голоден'.format(self.name))

    def state_of_calmness(self):
        if self.calmness == False:
            print('{} нужно успокоить\n'.format(self.name))
        else:
            print('{} спокоен'.format(self.name))

def age_test():
    for i in list_age:
        if parent.age - i > 16:
            print('условие возраста выполнено')
        else:
            print('условие не выполнено')
    print()

list_age = []
parent = Parent('Галина', 35)
child_1 = Child(name='Кирилл', age=10, hungry=True, calmness=True)
child_2 = Child(name='Максим', age=15, hungry=True, calmness=True)
list_age.append(child_1.age)
list_age.append(child_2.age)

test_age = age_test()

child_1.state_of_calmness()
child_1.state_of_hunger()
parent.feed_child()
































