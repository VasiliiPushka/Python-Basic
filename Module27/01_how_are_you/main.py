from typing import Callable
def how_are_you(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(input('Как дела? '))
        print('А у меня не очень! Ладно, держи свою функцию.')
        func(*args, **kwargs)
    return wrapper

@how_are_you
def test():
    print('<Тут что-то происходит...>')

test()

