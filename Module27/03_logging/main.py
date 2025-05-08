from typing import Callable
from datetime import datetime, date
import functools
import os


def logging(func: Callable) -> Callable:
    """Декоратор, логирующий работу кода"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        filepath = os.path.join('function_error.log')
        with open(filepath, 'a', encoding='utf-8') as func_error_file:
            print(f'\nВызывается функция {func.__name__}\t'
              f'позиционные аргументы {args}\t'
              f'именованные аргументы {kwargs}')

            try:
                result = func(*args, **kwargs)
                if result in ZeroDivisionError:
                    raise ZeroDivisionError
                elif result in TypeError:
                    raise TypeError
                else:
                    raise BaseException
            except ZeroDivisionError:
                func_error_file.write(f'{datetime.now()}\t{ZeroDivisionError.__name__}\t{func.__name__}\n')
            except TypeError:
                func_error_file.write(f'{datetime.now()}\t{TypeError.__name__}\t{func.__name__}\n')
            except BaseException:
                func_error_file.write(f'{datetime.now()}\t{BaseException.__name__}\t{func.__name__}\n')

            print('Функция успешно завершила логирование')
            return func
    return wrapper
@logging
def test_func(number: int):# небольшая функция для тестрования декоратора
    for n in range(number+1):
        result = 1000 / number - 1
        print(f'{round(result, 1)}\t {number}')
        number -= 1
@logging
def type_test(number: int):
    for i in range(number):
        print(i)

# Тестирование функций
my_func = test_func(3)
print()
my_type = type_test('3')











