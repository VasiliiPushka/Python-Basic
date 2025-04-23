def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number

def crypto(string):
    lst = []
    for i, j in enumerate(string):
        if is_prime(i) == True:
            lst.append(i)
    return lst




