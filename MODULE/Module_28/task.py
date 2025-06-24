# import math
# from abc import ABC, abstractmethod
#
# class Figure(ABC):
#     """ Базовый класс Фигура """
#
#     @abstractmethod
#     def __init__(self, radius: int, length: int) -> None:
#         self.radius = radius
#         self.length = length
#
# class MyMath:
#     @staticmethod
#     def circle_len(radius: int | float) -> float | int:
#         return 2 * math.pi * radius
#
#     @staticmethod
#     def circle_sq(radius: int | float) -> int | float:
#         return math.pi * radius ** 2
#
#     @staticmethod
#     def volume_qube(length: int | float) -> int | float:
#         return length ** 3
#
#     @staticmethod
#     def surface_area_sphere(radius: int | float) -> int | float:
#         return 4 * math.pi * radius ** 2
#
#
# circle = MyMath.circle_len(radius=4)
# circle_2 = MyMath.circle_sq(radius=4)
# cube = MyMath.volume_qube(length=5)
# sphere = MyMath.surface_area_sphere(radius=4)
#
# for figure in [circle, circle_2, cube, sphere]:
#     print(figure)


class HashTable:
    def __init__(self):
        # Создаём пустой список, который будет использоваться в качестве основы хеш-таблицы
        self.table = [None] * 10 # Изначально устанавливаем размер таблицы — 10 элементов

    def _hash_function(self, key):
        # Хеш-функция преобразует ключ в индекс таблицы
        # Простейшая хеш-функция — остаток от деления на размер таблицы
        return hash(key) % len(self.table)

    def _get_index(self, key):
        # Получаем индекс элемента в таблице по ключу
        hash_value = self._hash_function(key)
        # Если по этому индексу ещё нет элемента или ключи совпадают, возвращаем индекс
        if self.table[hash_value] is None or self.table[hash_value][0] == key:
            return hash_value
        # В противном случае применяем метод открытой адресации для разрешения коллизий
        else:
            index = (hash_value + 1) % len(self.table) # Используем линейное пробирование
            while self.table[index] is not None and self.table[index][0] != key:
                index = (index + 1) % len(self.table)
            return index

    def insert(self, key, value):
        # Вставляем элемент в хеш-таблицу
        index = self._get_index(key)
        self.table[index] = (key, value)

    def search(self, key):
        # Ищем элемент в хеш-таблице по ключу
        index = self._get_index(key)
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1] # Возвращаем значение элемента, если он найден
        else:
            return None # Возвращаем None, если элемент не найден

    def delete(self, key):
        # Удаляем элемент из хеш-таблицы по ключу
        index = self._get_index(key)
        if self.table[index] is not None and self.table[index][0] == key:
            self.table[index] = None # Просто удаляем элемент, присваивая ему значение None

# Создаём экземпляр хеш-таблицы
hash_table = HashTable()

# Вставляем элементы в хеш-таблицу
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

# Ищем элементы в хеш-таблице
print(hash_table.search("apple")) # Вывод: 1
print(hash_table.search("banana")) # Вывод: 2
print(hash_table.search("grape")) # Вывод: None

# Удаляем элемент из хеш-таблицы
hash_table.delete("banana")

# Проверяем, что элемент удалён
print(hash_table.search("banana")) # Вывод: None




