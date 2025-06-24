import time

class Parent:

    def __init__(self, name:str, age:int, child_list:list):
        self.name = name
        self.age = age
        self.child_list = child_list

    def info(self):
        child_name_list = []

        if len(self.child_list) == 1:
            print(f"name - {self.name} | age - {self.age} | "
                  f"baby's - {self.child_list[0].name}")

        else:
            for name in self.child_list:
                child_name_list.append(name.name)

            print(f"name - {self.name} | age - {self.age} | "
                  f"baby's - {child_name_list}")


    def calm_the_child_down(self):
        for child in self.child_list:
            if child.state_of_calm:
                print(f"{child.name} нужно успокоить\n"
                      f"аа-аа-аа-а")
                time.sleep(2)
                child.state_of_calm = False
                print(f"{child.name} успокоился")


    def feed_the_baby(self):
        for child in self.child_list:
            if child.hungry:
                print(f"{child.name} хочет кушать. Нужно покормить\t"
                      f" - открываем ротик")
                time.sleep(1)
                child.hungry = False
                print(f"{child.name} покушал")


class Children:

    def __init__(self, name:str, age:int, state_of_calm:bool, hungry:bool):
        self.name = name
        self.age = age
        self.state_of_calm = state_of_calm
        self.hungry = hungry

    def info(self):
        print(f'Name - {self.name} | age - {self.age} | '
              f'state_of_calm - {self.state_of_calm} | hunger - {self.hungry}')

    def name(self):
        print(f'{self.name}')


child_list = []
child = Children(name='Ваня', age=3, state_of_calm=True, hungry=True)
child_2 = Children(name='Соня', age=5, state_of_calm=True, hungry=False)

child_list.append(child)
child_list.append(child_2)

parent = Parent(name='Семен', age=33, child_list=child_list)
parent.calm_the_child_down()
parent.feed_the_baby()

child.info()
child_2.info()


