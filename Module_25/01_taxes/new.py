class Property:

    def __init__(self, worth:int):
        self.worth = worth

    def tax(self):
        return 0


class Apartment(Property):

    def __init__(self, worth:int):
        super().__init__(worth)

    def tax(self):
        tax = self.worth / 1000
        return tax


class Car(Property):

    def __init__(self, worth:int):
        super().__init__(worth)

    def tax(self):
        tax = self.worth / 200
        return tax

class CountryHouse(Property):

    def __init__(self, worth:int):
        super().__init__(worth)

    def tax(self):
        tax = self.worth / 500
        return tax

items = ['квартиры', 'автомобиля', 'дачи']
money = int(input("Введите кол-во денег: "))
prices = [int(input(f"Введите стоимость {items[i]}: ")) for i in range(3)]

apartment = Apartment(prices[0])
car = Car(prices[1])
country_house = CountryHouse(prices[2])

purchases = [apartment, car, country_house]

count = 0
for price in prices:

    if money >= price:
        print(f'Поздравляю, Вам хватает средств на покупку {items[count]}\n'
              f'налог - {purchases[count].tax()}')
    else:
        print(f"На покупку {items[count]} Вам не хватает {price - money}\n"
              f"налог - {purchases[count].tax}")
    count += 1









