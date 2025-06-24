import os

def walk_path(path:str):
    return os.walk(path, topdown=True, onerror=None, followlinks=False)


def count_sym(path: str):
    path = os.path.abspath(os.path.join('..', path))
    result = walk_path(path)


    for root, dirs, files in result:
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                line_count = 0

                with open (file_path, 'r', encoding='utf-8') as read_file:
                    for line in read_file:
                        stripped_line = line.lstrip()
                        if stripped_line and not stripped_line.startswith('#'):
                            line_count += 1
                yield line_count


a = count_sym('01_num_squares')
for i in a:
    print(i)