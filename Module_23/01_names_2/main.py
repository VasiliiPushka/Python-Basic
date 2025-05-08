line_count = 0
sym_sum = 0

try:
    with open('people.txt', 'r') as people_file:
        for i_line in people_file:
            line_count += 1
            lenght = len(i_line)
            if i_line.endswith('\n'):
                lenght -= 1
            if lenght < 3:
                print('Ошибка: менее 3х символов в строке {}'.format(line_count))
            sym_sum += lenght

except FileExistsError:
    print('Файл не найден')
finally:
    print('Найденная сумма символов:', sym_sum)
