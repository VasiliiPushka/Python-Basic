import random

original_list = [random.randint(1, 10) for i in range(10)]
print('Оригинальный список:', original_list)

bufer_list = []
new_list = []
count = 0
for ind, num in enumerate(original_list):
    bufer_list.insert(ind, num)
    count += 1
    if count == 2:
        new_list.append(tuple(bufer_list))
        count = 0
        bufer_list.clear()
print(new_list)















