class Water:

    def __str__(self):
        return "Water"

    def __add__(self, other):
        if isinstance(other, Air):
            return "Storm"
        elif isinstance(other, Fire):
            return "Steam"
        elif isinstance(other, Earth):
            return "Dirt"


class Air:

    def __str__(self):
        return "Air"

    def __add__(self, other):
        if isinstance(other, Earth):
            return "Dust"
        elif isinstance(other, Fire):
            return "Lightning"
        elif isinstance(other, Water):
            return "Storm"

class Fire:

    def __str__(self):
        return "Fire"

    def __add__(self, other):
        if isinstance(other, Air):
            return "Lightning"
        elif isinstance(other, Water):
            return "Steam"
        elif isinstance(other, Earth):
            return "Lava"

class Earth:

    def __str__(self):
        return "Earth"

    def __add__(self, other):
        if isinstance(other, Water):
            return "Dirt"
        elif isinstance(other, Fire):
            return ("Lava")
        elif isinstance(other, Air):
            return"Dust"

class Steam:
    def __str__(self):
        return "Steam"

class Storm:
    def __str__(self):
        return "Storm"

class Lightning:
    def __str__(self):
        return "Lightning"

class Dirt:
    def __str__(self):
        return "Dirt"

class Dust:
    def __str__(self):
        return "Dust"

class Lava:
    def __str__(self):
        return "Lava"

water = Water()
air = Air()

print(water + air)

    
