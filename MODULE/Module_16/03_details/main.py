shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
detail = input('Название детали: ')
count_detail = 0
total_price = []
price_detail = 0
for list in shop:
        if list[0] == detail:
                total_price.append(list[1])
                count_detail += 1
for price in total_price:
        price_detail += price

print('Кол-во деталей -', count_detail)
print('Общая стоимость -', price_detail)














