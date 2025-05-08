second_tour_list = []
count_people = 0
with open('first_tour.txt', 'r', encoding='utf-8') as file:
    for string in file:
        result = string.rstrip().split()
        if (len(result) >= 3) and (80 < int(result[2])):
            second_tour_list.append(result)
            count_people += 1
    file.close()

print('\nСодержимое файла second_tour.txt:\n')

with open('second_tour.txt', 'w', encoding='utf-8') as file:
    count = 0
    for lst in second_tour_list:
        name = lst[1][0] + '.'
        surname = lst[0]
        point = lst[2]
        count += 1
        file.write(str(count)+')' + ' ' + name + ' ' + surname + '\n')












