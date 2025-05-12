class Water:
    def __str__(self):
        return 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
class Air:
    def __str__(self):
        return 'Воздух'
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Fire):
            return Lightning()
class Earth:
    def __str__(self):
        return 'Земля'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
class Fire:
    def __str__(self):
        return 'Огонь'
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
class Storm:
    def __str__(self):
        return 'Шторм'
class Lava:
    def __str__(self):
        return 'Лава'
class Steam:
    def __str__(self):
        return 'Пар'
class Dirt:
    def __str__(self):
        return 'Грязь'
class Dust:
    def __str__(self):
        return 'Пыль'
class Lightning:
    def __str__(self):
        return 'Молния'

water = Water()
air = Air()
earth = Earth()
fire = Fire()
storm = water + air
steam = water + fire
dirt = water + earth
lightning = fire + air
dust = air + earth
lava = fire
print(storm, '\n', fire, '\n', dirt, '\n', lightning, '\n', dust, '\n', lava)
