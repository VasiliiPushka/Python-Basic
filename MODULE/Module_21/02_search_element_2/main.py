site = {
    'html': {
        'head': {
            'title': 'Мой сайт',
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(struct, key, depth):
    result = None
    if key in struct and (depth is None or depth >= 1):
        return struct[key]
    if depth is not None and depth >= 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth - 1)
    if result:
        return None

    elif depth is None:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth)
        if result:
            return result
    return result


user_key = input('Какой ищем ключ? ')

req = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if req == 'y':
    req_depth = int(input('Введите максимальную глубину: '))
else:
    req_depth = None

value = find_key(site, user_key, req_depth)
print('Значение ключа: ', value)





