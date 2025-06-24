import functools
from collections.abc import Callable
from typing import Optional


def check_permission(_func: Optional[Callable] = None, *, name: str) -> Callable:

    def check(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if name == 'admin':
                    result = func(*args, **kwargs)
                    return result
                elif name != 'admin':
                    raise PermissionError
            except PermissionError:
                print(f'{PermissionError.__name__}: у пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return wrapper
    return check


user_permissions = ['admin']


@check_permission(name='admin')
def delete_site():
    print('Удаляем сайт')


@check_permission(name='user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()


add_comment()
