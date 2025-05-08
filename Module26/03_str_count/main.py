import os
from collections.abc import Iterable

def gen_python_file(link: str) -> Iterable[str]:
    count_line = 0

    path = os.path.abspath(link)

    for filename in os.listdir(path):
        if filename.endswith('.py'):
            filepath = os.path.join(path, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    count_line += 1
                    if line.startswith('#') or line.startswith('\n'):
                        count_line -= 1
    yield count_line

path = gen_python_file('/Users/ekaterinakondrateva/PycharmProjects/practical work/basic 2.4 module')
for i in path:
    print(f'Общее кол-во строк во всех файлах  *.py: {i}')





