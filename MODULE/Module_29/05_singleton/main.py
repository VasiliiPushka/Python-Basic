import functools


def singlton(cls):
    """Декоратор класса. Превращает класс в синглтон(может иметь только 1 инстанс)"""

    @functools.wraps(cls)
    def wrapper_singlton(*args, **kwargs):
        if not wrapper_singlton.instance:
            wrapper_singlton.instance = cls(*args, **kwargs)
        return wrapper_singlton.instance

    wrapper_singlton.instance = None  # кэш
    return wrapper_singlton


@singlton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
