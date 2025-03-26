list_name = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

def good_list(list) -> list[str]:
    good_list = []
    for name in list:
        if list_name.index(name) % 2 == 0:
            good_list.append(name)
    return good_list

if __name__ == '__main__':
    print(good_list(list_name))
