def numerator(num):
    if num == 1:
        return 1

    num_minus_1 = numerator(num - 1)
    print(num_minus_1)

    return num_minus_1 + 1

print(numerator(10))