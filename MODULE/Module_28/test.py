import hashlib
class HashTable:
    def __init__(self):
        self.size = 10 # Размер хеш-таблицы
        self.table = [None] * self.size # Инициализация массива с None

    def _hash_function(self, key):
        return hash(key) % self.size # Хеш-функция, преобразующая ключ в индекс

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index] = value # Вставка значения по соответствующему индексу

    def get(self, key):
        index = self._hash_function(key)
        return self.table[index] # Получение значения по ключу

    def remove(self, key):
        index = self._hash_function(key)
        self.table[index] = None # Удаление значения по ключу

data = "Hello, World!"
hash_object = hashlib.sha256(data.encode())
hex_digest = hash_object.hexdigest()
print(hex_digest) # Выводит хеш-значение SHA-256


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














