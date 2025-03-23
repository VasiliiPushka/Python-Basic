start_list = []
shift_list = []
shift = int(input('Сдвиг: '))

for i in range(5):
    n = int(input('Введите число: '))
    start_list.append(n)

for number in range(5):
    shift_list.append(start_list[number - shift])
print('Изначальный список:', start_list)
print('Сдвинутый список:', shift_list)






