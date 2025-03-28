shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

def details():
    detail = input('Введите название детали: ')
    count_detail = 0
    total_price = 0
    for lst in shop:
        if lst[0] == detail:
            count_detail += 1
            total_price += lst[1]
    else:
        print('Деталь отсутствует')
    return (f"Кол-во деталей — {count_detail}\n"
            f"Общая стоимость — {total_price}")

if __name__ == "__main__":
    print(details())



