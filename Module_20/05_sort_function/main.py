
def tuple_sort(tpl):
    tpl_1 = tpl[:]
    tpl = list(tpl)
    for i_mn in range(len(tpl)):
        for current in range(i_mn, len(tpl)):
            if int(tpl[current]) == float(tpl[current]):
                if tpl[current] < tpl[i_mn]:
                    tpl[current],tpl[i_mn] = tpl[i_mn], tpl[current]
            else:
                return tpl_1
    tpl = tuple(tpl)
    return tpl


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tuple_sort(tpl))
print()












