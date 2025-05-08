class Property:
    def __init__(self, worth):
        self.worth = worth
    def cal_tax(self):
        tax = self.worth / 10000
        return tax

class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def cal_tax(self):
        tax = self.worth / 1000
        return '\nНалог на квартиру составляет: {} '.format(tax)

class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def cal_tax(self):
        tax = self.worth / 200
        return '\nНалог на автомобиль составляет: {} '.format(tax)
class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def cal_tax(self):
        tax = self.worth / 500
        return '\nНалог на дачу составляет: {} '.format(tax)


home = Apartment(worth=10000000)
car = Car(worth=1500000)
country_house = CountryHouse(worth=1000000)
print(home.cal_tax())
print(car.cal_tax())
print(country_house.cal_tax())
