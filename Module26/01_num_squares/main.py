from collections.abc import Iterable

print('-' * 25, 'Класс-Итератор', '-' * 25)
class Iteration:
    def __init__(self, number):
        self.number = number
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.number:
            self.start += 1
            return self.start ** 2
        raise StopIteration

num = Iteration(5)
for i in num:
    print(i, end=' ')

print()

print('-' * 25, 'Генераторное выражение', '-' * 25)

square_gen = ((i+1) ** 2 for i in range(int(input('Введите число: '))))
for i in square_gen:
    print(i, end=' ')

print()

print('-' * 25, 'Функция генератор', '-' * 25)

def gen_func(number: int) -> Iterable[int]:
    for i in range(number):
        yield (i + 1) ** 2

n = gen_func(5)
for i in n:
    print(i, end=' ')