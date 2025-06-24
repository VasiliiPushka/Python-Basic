quantity = int(input('Введите кол-во заказов: '))

order_dict = {}
for order in range(quantity):

    name_order = input(f'{order + 1}й заказ: ').split()
    pizza_dict = {}
    if name_order[0] not in order_dict:
        order_dict[name_order[0]] = pizza_dict
        pizza_dict[name_order[1]] = int(name_order[2])

    elif name_order[0] in order_dict:
        for i_values in order_dict[name_order[0]]:
            if i_values == name_order[1]:
                order_dict[name_order[0]][name_order[1]] += int(name_order[2])
                break
        else:
            order_dict[name_order[0]][name_order[1]] = int(name_order[2])

for name in order_dict:
    print(f'{name}:')
    for i_values in order_dict[name]:
        print(f'\t{i_values}: {order_dict[name][i_values]}')







