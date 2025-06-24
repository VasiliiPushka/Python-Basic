import time
import functools
from typing import Callable, Any

def timer(func: Callable) -> Callable:

    """
    Декоратор, который замедляет выполнение декорируемой функции на 2 секунды.
    Args:
        func: Функция, которую нужно декорировать.

    Returns: Ссылка на функцию-обёртку.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        """
               Обёртка для декорируемой функции, осуществляющая задержку перед вызовом.
               Задерживает выполнение на 2 секунды, а затем вызывает оригинальную функцию
               с переданными ей аргументами.
               Args:
                   *args: Позиционные аргументы, передаваемые в декорируемую функцию.
                   **kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
               Returns: Результат, возвращаемый декорируемой функцией.
               """

        time.sleep(4)
        result = func(*args, **kwargs)

        return result
    return wrapped_func