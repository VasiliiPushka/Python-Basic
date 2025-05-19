import os
from collections.abc import Iterable

def gen_files_path(link: str)-> Iterable[str]:

    search = input('Введите имя файла: ')

    for dirpath, dirnames, filenames in list(os.walk(link)):
        for i_file in filenames:
            yield str(dirpath) + '//' + i_file
            if i_file == search:
                return


p = gen_files_path('/Users/ekaterinakondrateva/PycharmProjects/practical work')
for i_file in p:
    print(i_file)
