a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
five_in_a = a.count(5)
print(five_in_a)

for i in a:
    if i == 5:
        a.remove(5)
print(a)

a.extend(c)
three_in_a = a.count(3)
print(three_in_a)
print(a)