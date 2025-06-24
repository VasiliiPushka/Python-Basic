def new_sum(massiv):
    summ = 0
    count = 0
    if massiv == [] or massiv == ():
        return summ
    elif isinstance(massiv[count], int):
        summ += massiv[count]
    elif isinstance(massiv[count], list) or isinstance(massiv[count], tuple):
        for i in massiv[count]:
            if isinstance(i, int):
                summ += i
            elif isinstance(i, list) or isinstance(i, tuple):
                for j in i:
                    summ += j
    return summ + new_sum(massiv[count+1::])


n = ([[1, 2, [3]], [1], 3, 6])
print(new_sum(n))
