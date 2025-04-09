array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
array_1 = set(array_1)
array_2 = set(array_2)
array_3 = set(array_3)

new_array = [i for i in array_1
             for j in array_2
             for k in array_3
             if i == j == k]
print('Элементы, которые есть в каждом списке:')
print(f'\t1) решения с множествами: {array_1 & array_2 & array_3}')
print(f'\t2) решение без множеств: {new_array}')

print('\nЭлементы, из первого списка, которых нет во втором и третьем списках:')
print(f'\t1) с использованием множеств: {array_1 - array_2 - array_3}')

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

n = []
for i in array_1:
    if i not in array_2 + array_3:
        n.append(i)
print(f'\t2) решение без множеств: {n}')
















