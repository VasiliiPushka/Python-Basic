def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr],my_list[i_mn] = my_list[i_mn], my_list[curr]

n = int(input('Сколько чисел будет в списке? '))
number = []
for _ in range(n):
    i = int(input('Введите число: '))
    number.append(i)

print('Изначальный список:', number)
selection_sort(number)
print('Отредатированный список:', number)


