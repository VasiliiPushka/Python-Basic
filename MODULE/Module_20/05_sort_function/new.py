def tpl_sort(korteg):
    lst = list(korteg)
    sort_list = sorted(lst)
    sort_tuple = tuple(sort_list)
    return sort_tuple

a = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(a))