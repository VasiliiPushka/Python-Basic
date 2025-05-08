import os
from collections.abc import Iterable

def error_log_generator(link: str) -> Iterable[str]:

    path = os.path.join(link)

    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            filepath = os.path.join(path, filename)
            with open(filepath, 'r', encoding='utf-8') as read_file:
                for line in read_file:
                    if line.startswith('ERROR'):
                        yield line


input_file_path = os.path.join('data')
output_file_path = os.path.join('data/error.log')


with open(output_file_path, 'w', encoding='utf-8') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")




# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)

# Документация по join https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/







