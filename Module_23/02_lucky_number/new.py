import random
sum_number = 0

try:
    while sum_number < 777:
        random_number = random.randint(1, 13)
        print(f"Случайное число {random_number}")
        if random_number == 13:
            raise random.choice([BaseException, ValueError, TypeError, RuntimeError])("Вас постигла неудача!")

        elif random_number != 13:
            with open('out_file.txt', 'a', encoding='utf-8') as file:
                number = int(input("Введите число: "))
                file.write(str(f"{number}\n"))
                sum_number += number
        else:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')

except ValueError:
    print('введите корректное число!!')



print('Содержимое файла out_file.txt')
with open('out_file.txt', 'r') as out_file:
    for i_line in out_file:
        print(i_line.rstrip())








