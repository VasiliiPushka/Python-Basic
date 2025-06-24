def quick_sort(massiv):
    if len(massiv) < 2:
        return massiv
    else:
        pivot = massiv[-1]
        less = [i for i in massiv[:-1] if i < pivot]
        greater = [i for i in massiv[:-1] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

massiv = [5, 8, 9, 4, 2, 9, 1, 8]
print(quick_sort(massiv))