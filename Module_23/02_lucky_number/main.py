import random

sum_count = 0
number = 777
total_try = 0
try:
    with open('out_file.txt', 'w') as out_file:
        while sum_count < number:
            trying = random.randint(1, 13)
            total_try += 1
            if trying != 13:
                user_num = int(input('Введите число: '))
                out_file.write(str(user_num) + '\n')
                sum_count += user_num
            elif trying == 13:
                raise BaseException('Вас постигла неудача!')
        else:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
except ValueError:
    print('Измените значение с int на str')

print('Содержимое файла out_file.txt')
with open('out_file.txt', 'r') as out_file:
    for i_line in out_file:
        print(i_line.rstrip())






