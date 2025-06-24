number_order = int(input("Введите кол-во заказов: "))

order_dict = {}

for i in range(number_order):
    order_list = input(f"{i+1}-й заказ: ").split()
    name = order_list[0]
    pizza = order_list[1]
    quantity = order_list[2]
    quantity = int(quantity)

    if name not in order_dict:
        order_dict[name] = {}

    if pizza not in order_dict[name]:
        order_dict[name][pizza] = 0

    order_dict[name][pizza] += quantity

for name in order_dict:
    print(f"{name}")
    for pizza in order_dict[name]:
        print(f"\t{pizza}: {order_dict[name][pizza]}")





















