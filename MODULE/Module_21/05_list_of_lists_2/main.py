def list_of_lists_2(massiv):
    summ_list = []
    count = 0
    if massiv == []:
        return summ_list
    elif isinstance(massiv[count], int):
        summ_list.append(massiv[count])
    elif isinstance(massiv[count], list):
        for i in massiv[count]:
            if isinstance(i, int):
                summ_list.append(i)
            elif isinstance(i, list):
                for j in i:
                    summ_list.append(j)
    return summ_list + list_of_lists_2(massiv[count + 1::])

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(list_of_lists_2(nice_list))






