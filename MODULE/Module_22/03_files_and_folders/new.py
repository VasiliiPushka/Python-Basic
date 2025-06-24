import os

path = os.path.abspath(os.path.join('..', '..'))

def print_dir(path):
    print(f'Путь до каталога: {path}')

    count_dir = 0
    count_file = 0
    size = 0

    for i_elem in os.listdir(path):
        count_dir += 1
        i_size = os.path.getsize(path)
        size += i_size
    print('кол-во подкаталогов:'.title(), count_dir)
    return f'размер каталога: {size} (в Кб)'

print(print_dir(path))



