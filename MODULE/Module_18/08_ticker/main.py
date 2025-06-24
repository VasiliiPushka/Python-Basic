string_1 = input('Первая строка: ')
string_2 = input('Вторая строка: ')

for shift in range(len(string_1)):
    char_list = [(string_2[(string_2.index(sym) + shift) % len(string_2)]) for sym in string_2]
    new_str = ''
    for i_elem in char_list:
        new_str += i_elem
    if new_str == string_1:
        print('Первая строка получается из второй со сдвигом', shift)
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
