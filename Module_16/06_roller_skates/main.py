size_roller =[]
size_foot =[]
count = 0

quantity_roller = int(input('Кол-во коньков: '))
for size in range(quantity_roller):
    print(f'Размер {size + 1}-й пары:', end=' ')
    size_rol = int(input())
    size_roller.append(size_rol)

people = int(input('\nКол-во людей: '))
for size_people in range(people):
    print(f'Размер {size_people + 1}-го человека:', end=' ')
    size_ft = int(input())
    size_foot.append(size_ft)
size_roller.sort()
size_foot.sort()
print(size_roller)
print(size_foot)
for foot in size_foot:
    for size in size_roller:
        if foot == size:
            size_roller.remove(size)
            count += 1
            break


print('Наибольшее кол-во людей, которые могут взять ролики:', count)





