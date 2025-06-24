# программа, которая избавляется от:
# Двух символов # в начале информационных сообщений;
# Строк, заканчивающихся тремя символами @.
# Формат ввода
# Вводятся строки отчёта. Признаком завершения ввода считается пустая строка.
#
# Формат вывода
# Очищенные данные.

def cleaner():
    # Читаем все строки ввода до пустой строки
    lines = []
    while True:
        line = input().strip('\n')  # Убираем символы перевода строки
        if line == "":
            break
        lines.append(line)

    # Обрабатываем каждую строку
    for line in lines:
        # Пропускаем строки, заканчивающиеся на @@@
        if line.endswith('@@@'):
            continue

        # Удаляем ## в начале строки, если они есть
        if line.startswith('##'):
            line = line[2:]

        # Выводим обработанную строку
        print(line)

def palindrom():
    word = input().strip()
    if word == word[::-1]:
        print("YES")
    else:
        print("NO")


# task list comprehensions

def get_hair_price(percent, price):
    return round(price * (1 + percent / 100), 2)

price_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_percent = int(input('Повышение за 1й год: '))
second_percent = int(input('Повышение за 2й год: '))

prices_first = [get_hair_price(first_percent, i_price) for i_price in price_now]
prices_second = [get_hair_price(second_percent, i_price) for i_price in price_now]

print(sum(price_now), sum(prices_first), sum(prices_second))

if __name__ == "__main__":
    palindrom()