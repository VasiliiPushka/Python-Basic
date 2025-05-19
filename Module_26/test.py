#
#
# string = 'строка'
#
# def iterable(iter_object):
#     iterator = iter(iter_object)
#     try:
#         while True:
#             item = next(iterator)
#             print(item)
#     except StopIteration:
#         print("Конец итерации, элементов больше нет")
#
# iterable(string)


class Fibonacci:

    """ Итератор последовательности Фибоначчи из N элементов """

    def __init__(self, number):
        self.counter = 0
        self.cur_value = 0
        self.next_value = 1
        self.number = number

    def __iter__(self):
        self.counter = 0
        self.cur_value = 0
        self.next_value = 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number :
                raise StopIteration()
            self.cur_value, self.next_value = self.next_value, self.next_value + self.cur_value

        return self.cur_value

fib_iterator = Fibonacci(10)
for i_value in fib_iterator:
    print(i_value, end='\n')


print(13 in fib_iterator)


def fibonacci(number):
    current_value = 0
    next_value = 1
    for _ in range(number):
        yield current_value
        current_value, next_value = next_value, current_value + next_value

        if current_value > 10 ** 6:
            return


def square(numbers):
    for num in numbers:
        yield num ** 2



fib_seq = fibonacci(number=100000000)
for i_value in fib_seq:
    print(i_value)

# генератор от генератора
print(f'\n'
      f'{sum(square(fibonacci(number=5000)))}')












