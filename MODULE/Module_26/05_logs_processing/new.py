import os

def count_errors():
    root = os.path.abspath('data')
    file_path = os.path.join(root, 'work_logs.txt')

    with open(file_path, 'r', encoding='utf') as read_file:
        with open('error.log', 'a', encoding='utf-8') as error_file:
            for string in read_file:
                if string.startswith('ERROR'):
                    error_file.write(string)


check = count_errors()