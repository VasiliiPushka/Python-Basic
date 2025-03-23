n = int(input('Введите число: '))
numbers = []
for number in range(1, n + 1):
    if (number % 2 - 1) == 0:
        numbers.append(number)
print(numbers)