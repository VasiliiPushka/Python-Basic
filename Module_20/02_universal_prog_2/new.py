def is_prime(index):
    if index <= 1:
        return False
    elif index == 2:
        return True
    elif index > 2 and index % 2 == 0:
        return False
    for i in range(3, int(index ** 0.5) + 1, 2):
        if index % i == 0:
            return False
    return True

def crypto(iter_object):
    return_list = []
    for i, sym in enumerate(iter_object):
        if is_prime(i):
            return_list.append(sym)
    return return_list

print(crypto('О Дивный Новый мир!'))
