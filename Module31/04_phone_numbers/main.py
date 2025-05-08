test_list = ['9999999999', '999999-999', '99999x9999']

count_number = 0

for number in test_list:
    count_number += 1
    if number.startswith(('8', '9')) and len(number) == 10 and (str.isdigit, number):
        print(f'{count_number}-й номер: все в порядке')
    else:
        print(f'{count_number}-й номер: не подходит')

