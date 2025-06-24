from typing import Callable
import functools
def decorator_with_args_for_any_decorator(decor: Callable) -> Callable:
    """Декоратор. Дает возможность другому декоратору принимать произвольные аргументы"""

    def decorator_maker(*args, **kwargs) -> Callable:

        def wrapper(func: Callable) -> Callable:
            return decor(func, *args, **kwargs)

        return wrapper

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print(f'Переданные арги и кварги в декоратор {args} {kwargs}')
        result = func(*func_args, **func_kwargs)
        return result

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
