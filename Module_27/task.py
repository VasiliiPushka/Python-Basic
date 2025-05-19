import time
import functools
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    """ Декоратор """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = round((end - start), 4)
        print(f'функция работала - {run_time}')

        return result
    return wrapped_func


def logging(func: Callable) -> Callable:

    """
    Декоратор, логирующий работу кода
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Callable:
        print(f'\nВызывается функция {func.__name__}\t Позиционные аргументы - {args}\t'
              f'Именованные аргументы - {kwargs}')

        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} успешно завершила работу')
        return result
    return wrapped_func

@logging
@timer
def squared_sum() -> int:
    number = 100
    result = 0

    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])

    return result

@timer
@logging
def cubes_sum(number: int) -> int:
    result = 0

    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])

    return result


my_sum = squared_sum()
print(my_sum)

my_cubes_sum = cubes_sum(200)
print(my_cubes_sum)


