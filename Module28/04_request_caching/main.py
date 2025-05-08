from typing import Any

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache_dict = {}
        self.key = None

    @property
    def cache(self) -> Any:
        if len(self.cache_dict) > 0:
            key = input('Введите ключ: ')
            if key in self.cache_dict:
                return f"{self.cache_dict[key]}"
            else:
                return 'Такого ключа в LRU Cache не существует'
        return "LRU Cache - пуст."

    @cache.setter
    def cache(self, new_elem: Any) -> Any:
        if len(self.cache_dict) >= self.capacity:
            key = next(iter(self.cache_dict))
            del self.cache_dict[key]
        self.cache_dict[new_elem[0]] = new_elem[1]

    def print_cache(self) -> Any:
        print('LRU Cache')
        for key, value in self.cache_dict.items():
            print(f'{key} : {value}')
        return f''



# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# Выводим текущий кэш
print(cache.print_cache())  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.cache, '\n')# value2


# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
print(cache.print_cache())  # key2 : value2, key3 : value3, key4 : value4
