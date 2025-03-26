
people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print('Значит выбывает каждый', number, 'человек')


people_list = list(range(1, people + 1))
del_people = 0

while len(people_list) > 1:
    del_people = (del_people + number - 1) % len(people_list)
    print('\nТекущий круг людей:', people_list)
    print(f'Выбывает человек под номером', people_list[del_people])
    del people_list[del_people]

print('\nОстался человек под номером', people_list[0])






# while len(people_list) > 1:
#     for i in range(number - 1):
#         people_list.append(people_list[i])
#     del people_list[:number]
# print(people_list)










