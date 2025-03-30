word = input('Введите строку: ')
sym_list = list(word)
count = 0
result = word[:len(sym_list)]

for i in result:
    count += 1
    if i == 'h':
        sym_list.remove(i)
        break

result = result[count::]
result = result[::-1]

for j in result:
    count += 1
    if j == 'h':
        sym_list.remove(j)
        break

result = result[count-1::]
print('Развернутая последовательность между первым и последним h:', result)