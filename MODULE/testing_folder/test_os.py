import os
#
# abs_path = os.path.abspath('admin.bat')
# path = os.path.join('Python-Basic', 'testing_folder' ,'admin.bat')
# print()
# print(abs_path,'\n',
#       path)
#
# print()
# abs_path = os.listdir(os.path.abspath('../'))
# for dir in abs_path:
#     print(dir)
#
# print()
# current_path = os.sep
#
# print(current_path)
import os
from site import abs_paths

#
#
# def find_file(cur_path, file_name):
#     print("переходим:", cur_path)
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print("    смотрим", path)
#
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):
#             print("это директория")
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
# file_path = find_file(os.path.abspath(os.path.join('..', '..', 'Python-Basic')), 'task_2.py')
# if file_path:
#     print('Абслоютный путь к файлу: ', file_path)
# else:
#     print('файл не найден')
#
#
# def path_chek(path):
#     if os.path.isdir(abs_path):
#         print('Это директория')
#     elif os.path.isfile(abs_path):
#         size = os.path.getsize(abs_path)
#         print('Это файл\n',
#           f'размер файла: {size}')
#     elif os.path.islink(abs_path):
#         print('Это ссылка')
#
# abs_path = os.path.abspath(os.path.join('test_os.py'))
# path_chek(abs_path)
# print()
#
#
# def find_file(cur_path, file_name):
#     # print(f"Запуск поиска в папке: {os.path.join(os.path.abspath(cur_path))}")
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         # print("Проверяется путь: ", path)
#
#         if file_name == i_elem:
#             print(os.path.abspath(path))
#         if os.path.isdir(path):
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
# find_file('..', 'new.py')
#
#
# file_path = find_file(os.path.abspath(os.path.join('..', '..', 'Python-Basic')), 'new.py')

