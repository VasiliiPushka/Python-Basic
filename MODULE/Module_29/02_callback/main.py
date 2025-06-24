import functools
from typing import Callable, Dict, Any

app: Dict[str, Callable] = dict()


def callback(route: str) -> Callable:
    def decorator_callback(func: Callable) -> callable:
        app[route] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator_callback


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


print('Основной код: ')
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
