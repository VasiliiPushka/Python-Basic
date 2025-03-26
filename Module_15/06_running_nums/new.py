shift = int(input("Введите сдвиг: "))
start_list = []
shift_list = []
length = int(input('Введите длину списка: '))

for i in range(length):
    num = int(input("Введите число: "))
    start_list.append(num)

for number in range(length):
    shift_list.append(start_list[number - shift])
print(f"{start_list},\n{shift_list}")




