goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

total_store = dict()
quantity = list()

for key, values in store.items():
    count = 0
    for value in values:
        if key not in total_store:
            total_store[key] = value['quantity'] * value['price']
            count = value['quantity']
        else:
            total_store[key] += value['quantity'] * value['price']
            count += value['quantity']
    quantity.append(count)
    count = 0

result = {}

for key_s, value_s in goods.items():
    for key_t, value_t in total_store.items():
        if value_s == key_t:
            result[key_s] = value_t

count = 0
for i in goods.keys():
    print(f"{i} - {quantity[count]} штук, стоимость {result[i]} рубля")
    count += 1







