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

total_price = 0
quantity = 0
tot_price = []
tot_quantity = []


for store_id in store.values():
    for quan_price in store_id:
        total_price += quan_price['price'] * quan_price['quantity']
        quantity += quan_price['quantity']
    tot_price.append(total_price)
    tot_quantity.append(quantity)
    total_price = 0
    quantity = 0

count = 0
for good in goods:
    print(f'{good} - {tot_quantity[count]} штук, стоимость {tot_price[count]} рублей')
    count += 1
