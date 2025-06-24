class Iterator:

    """ Итератор квадратов чисел """

    def __init__(self, number:int):
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.number:
            raise StopIteration()
        self.counter += 1
        return self.counter ** 2


def generation(number:int):
    counter = 1
    while counter < number:
        yield counter ** 2
        counter += 1


squad_num = (i**2 for i in range(1, int(input("введите число: ")) +1 ))
for i in squad_num:
    print(i)

num = int(input("введите число: "))
num_iterator = Iterator(num)
for i in num_iterator:
    print(i)

# for i in generation(num):
#     print(i)







