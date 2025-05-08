import time
from typing import Callable
import functools
from datetime import datetime


def timer(cls, func: Callable, date_format) -> Callable:
    """Декоратор метода. Получает метод как функцию
    выводит время и дату запуска метода
    при завершении указывает время работы"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        format = date_format
        for sym in format:
            if sym.isalpha():
                format = format.replace(sym, '%' + sym)
        print(f'Запускается {cls.__name__}.{func.__name__}. Дата и время запуска {datetime.now().strftime(format)}')
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Завершение {cls.__name__}.{func.__name__}. Время работы {finish - start} секунд')

        return result

    return wrapper


def log_methods(date_format: str):
    """Декоратор класса. Получает другой декоратор
    и применяет его ко всем методам класса"""

    @functools.wraps(date_format)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = timer(cls, cur_method, date_format)
                setattr(cls, i_method_name, decorated_method)
        return cls

    return decorate


@log_methods('b d Y - H:M:S')
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods('b d Y - H:M:S')
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
