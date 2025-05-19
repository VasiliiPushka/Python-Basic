import functools
from typing import Callable, Any


def counter(func: Callable) -> Callable:


    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} была вызвана {wrapper.count} раз')
        return result

    wrapper.count = 0
    return wrapper

@counter
def test():
    print('test')

test()
test()
test()






