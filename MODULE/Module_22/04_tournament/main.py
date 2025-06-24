lines = ['80', 'Ivanov Serg 80', 'Sergeev Petr 92', 'Petrov Vasiliy 98', 'Vasiliev Maxim 78']

with open('first_tour.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')
print('Содержимое файла first_tour.txt:')
with open('first_tour.txt', 'r') as file:
    for line in lines:
        print(line)
file.close()

print('\nСодержимое файла second_tour.txt:')

file_2_list = []
with open('first_tour.txt', 'r') as file:
    for line in file:
        file_2_list.append(line.split())
file.close()

with open('second_tour.txt', 'w') as file_2:
    count = 0
    for i_line in file_2_list[1::]:
        if i_line[2] >= '90':
            for sym_name in i_line[1]:
                name = sym_name + '.'
                count += 1
                break
            file_2.write(str(str(count) + ')' + ' ' + name + ' ' + i_line[0] + ' ' + i_line[2] + '\n'))
file_2.close()














