def matreshka(number):
    if number >= 1:
        matreshka(number - 1)
        print(number)

n = int(input('Введите число: '))
matreshka(n)