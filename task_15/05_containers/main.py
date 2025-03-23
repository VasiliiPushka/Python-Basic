
box_list = []
index_count = 0

box = int(input('Введите кол-во контейнеров: '))
for weight in range(box):
    while True:
        weight_box = int(input('Введите вес контейнера: '))
        if weight_box <= 200:
            box_list.append(weight_box)
            break
        print('Ошибка. Введите вес контейнера меньше 200 кг.')

box_list.sort(reverse=True)
new_box_weight = int(input('Введите вес нового контейнера: '))

box_list.append(new_box_weight)
box_list.sort(reverse=True)

for box in box_list:
    index_count += 1
    if box < new_box_weight:
        break

print('Номер, который получит новый контейнер:', index_count)







