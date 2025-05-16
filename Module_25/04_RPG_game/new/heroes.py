import random


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
# Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель

    def __init__(self, name):
        super().__init__(name)
        self.__magic_power = self.get_power() * 3
        self.__max_hp_hero = 150


    def attack(self, target):
        target.take_damage(self.get_power() * 0.5)

    def take_damage(self, damage):
        super().take_damage(damage)
        self.set_hp(self.get_hp() - damage * 1.2)


    def hill(self, target):
        target.set_hp(target.get_hp() + self.__magic_power)

    def get_magic_power(self):
        return self.__magic_power

    def __str__(self):
        return (f"{self.name} | текущее здоровье - {self.get_hp()} | "
                f"урон - {self.get_magic_power()} |is Alive - {self.is_alive()}")

    def get_hero_max_hp(self):
        return self.__max_hp_hero

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends=friends, enemies=enemies)

        target_of_healing = friends[0]
        min_health = target_of_healing.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_healing = friend
                min_health = target_of_healing.get_hp()

        if min_health < 120:
            print(f'Исцеляю {target_of_healing.name}')
            self.hill(target_of_healing)
        else:
            if not enemies:
                return
            print(f'Атакую ближнего врага {enemies[0]}')
            self.attack(enemies[0])
        print('\n')




class Tank(Hero):
    ...
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель

    def __init__(self, name, protection_index = 1):
        super().__init__(name)
        self.protection_index = protection_index
        self.shield = False
        self.__max_hp_hero = 150

    def attack(self, target):
        target.take_damage(self.get_power() * 0.5)

    def take_damage(self, damage):
        super().take_damage(damage)
        self.set_hp(self.get_hp() - (damage / self.protection_index))

    def shield_up(self):
        if self.shield is False:
            self.shield = True
            self.protection_index *= 2
            self.set_power(self.get_power() / 2)

    def shield_dawn(self):
        if self.shield is True:
            self.shield = False
            self.protection_index /= 2
            self.set_power(self.get_power() * 2)

    def __str__(self):
        return (f"{self.name} | текущее здоровье - {self.get_hp()} | "
                f"урон - {self.get_power()} | is alive - {self.is_alive()}")

    def get_hero_max_hp(self):
        return self.__max_hp_hero

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)

        if self.get_hp() > self.get_hero_max_hp() * 0.9:
            print(f"{self.name} - Атакую того, кто стоит ближе - {enemies[0].name}")
            self.attack(enemies[0])

        elif self.get_hp() < self.get_hero_max_hp() * 0.9:
            self.shield_up()
            print(f"{self.name} - поднял щит!", end='\n')

        elif self.shield is True and self.get_hp() > self.get_hero_max_hp() * 0.9:
            print(f"{self.name} - опустил щит, чтобы в след ходу нанести полный урон урон")
            self.shield_dawn()

        elif not enemies:
            return



class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель

    def __init__(self, name, power_multiply = 1):
        super().__init__(name)
        self.power_multiply = power_multiply
        self.__max_hp_hero = 150

    def attack(self, target):
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_dawn()

    def take_damage(self, damage):
        super().take_damage(damage)
        self.set_hp(self.get_hp() - damage * (self.power_multiply / 2))

    def power_up(self):
        self.power_multiply *= 2

    def power_dawn(self):
        self.power_multiply /= 2

    def get_hero_max_hp(self):
        return self.__max_hp_hero

    def __str__(self):
        return (f"{self.name} | текущее здоровье - {self.get_hp()} | "
                f"урон - {self.get_power()} | is alive - {self.is_alive()}")

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)

        target_of_kill = enemies[0]
        min_health = target_of_kill.get_hp()
        for enemy in enemies:
            if enemy.get_hp() < min_health:
                target_of_kill = enemy
                min_health = target_of_kill.get_hp

        if self.power_multiply == 1:
            print(f'POWER UP!!!')
            self.power_up()
        elif self.power_multiply == 2:
            print(f'Атакую {target_of_kill.name}')
            self.attack(target_of_kill)
        else:
            if not enemies:
                return
        print('\n')








