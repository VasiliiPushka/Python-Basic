import os
user_path = input('Введите путь до каталога:')
def print_dirs(path):
    print('путь до каталога:'.title(), path)
    count_dir = 0
    count_file = 0
    size = 0
    for i_elem in os.listdir(path):
        count_dir += 1
        i_size = os.path.getsize(path)
        size += i_size
    print('кол-во подкаталогов:'.title(), count_dir)
    print('размер каталога:'.title(), size)


print_dirs(user_path)