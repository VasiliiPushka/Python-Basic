import random

original_list = [random.randint(0, 100) for i in range(10)]
new_list = []
count = 0
small_list = []
for i in original_list:
    count += 1
    small_list.append(i)
    if count == 2:
        new_list.append(tuple(small_list))
        count = 0
        small_list.clear()
print(new_list)
