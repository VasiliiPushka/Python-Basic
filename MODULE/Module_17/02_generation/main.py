n = int(input('Введите число: '))
list_n = [(1 if i % 2 == 0 else i % 5) for i in range(n)]
print(list_n)