import time
from typing import Callable
import functools
def slaw_timer(func: Callable) -> Callable:
    """Декоратор, перед выполнинием функции ждет 5 секунд"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        second = 5
        while second > 0:
            print(second)
            time.sleep(1)
            second -= 1
        res = func(*args, **kwargs)
        return res
    return wrapper


@slaw_timer
def web_site():
    """Функция, выполняющая работу сайта"""
    print('работа сайта')

print(web_site.__doc__)
web_site()
