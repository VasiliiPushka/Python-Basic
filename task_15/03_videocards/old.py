nvidia = []
new_nvidia = []

quntity = int(input('Количесво видеокарт: '))
for i in range(quntity):
    name = int(input('Ведеокарта: '))
    nvidia.append(name)
print('Старый список видеокарт:', nvidia)

for number in nvidia:
    if number / max(nvidia) != 1:
        new_nvidia.append(number)
print('Новый список видеокарт:', new_nvidia)





