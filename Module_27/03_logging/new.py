import datetime
import functools
from typing import Callable, Any

def logging(func: Callable) -> Callable:
    """
        Декоратор для логирования информации о функции, её документации
        и обработки ошибок при выполнении.


        При каждом вызове декорируемой функции он выводит на экран её название
        и документацию. В случае возникновения исключения информация об ошибке
        записывается в файл `function_errors.log`.
        Args:
            func: Функция, которую нужно декорировать.


        Returns: Ссылка на функцию-обёртку.


        """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        """
                Обёртка для декорируемой функции, осуществляющая логирование и обработку ошибок.
                Args:
                    *args: Позиционные аргументы, передаваемые в декорируемую функцию.
                    **kwargs: Именованные аргументы, передаваемые в декорируемую функцию.


                Returns: Результат, возвращаемый декорируемой функцией.


                """

        try:
            print(f'\nВызывается функция {func.__name__}\n'
                  f'Документация: {func.__doc__}\n'
                  f'Позиционные аргументы: {args}\n'
                  f'Именованные аргументы: {kwargs}')
            result = func(*args, **kwargs)
            print(f'Функция {func.__name__} успешно завершила работу')
            return result
        except Exception as e:
            error_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_msg = f"{error_time} | Ошибка в функции {func.__name__}: {e}\n"
            with open("function_errors.log", 'a', encoding='utf-8') as log_file:
                log_file.write(error_msg)
            return None
    return wrapped_func