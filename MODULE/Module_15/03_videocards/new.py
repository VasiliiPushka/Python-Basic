def sorted_list(num:int) -> list[int]:
    old_list = []
    new_list = []
    for i in range(quan):
        model = int(input('Введиет модель: '))
        old_list.append(model)

    for model in old_list:
        if model != max(old_list):
            new_list.append(model)
    return new_list

if __name__ == '__main__':
    quan = int(input('Введите кол-во видеокарт: '))
    print(sorted_list(quan))
