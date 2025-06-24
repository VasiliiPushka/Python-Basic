a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
count_5 = 0
count_3 = 0
count = 0
a.extend(b)
for i in a:
    if i // 5 == 1:
        count_5 += 1
print('Кол-во цифр 5 при первом объединении:', count_5)
for i in a:
    if i == 5:
        a.remove(5)
a.extend(c)
for i in a:
    if i == 3:
        count_3 += 1
print('Кол-во цифр 3 при втором объединении:', count_3)
print('Итоговый список:', a)
















