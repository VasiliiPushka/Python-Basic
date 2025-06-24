name_fail = input('Введите название файла: ')
prefix = ('@', '#', '$', '%', '^', '&', '*', '(', ')', '/')
if name_fail.startswith(prefix):
    print('название начинается на один из специальных символов.')
elif not name_fail.endswith('.txt') or name_fail.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно')
