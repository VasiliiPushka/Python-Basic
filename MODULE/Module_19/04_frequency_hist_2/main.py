def histogramm(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

def invert_histogramm(hist):
    invert_dict = {}
    for key in hist.keys():
        if hist[key] not in invert_dict:
            invert_dict[hist[key]] = [key]
        else:
            invert_dict[hist[key]].append(key)
    return invert_dict

text = input('Введите текст: ')
hist = histogramm(text)
print(f'Оригинальный словарь частот: {hist}')

invert = invert_histogramm(hist)
for i in invert:
    print(f'{i}: {invert[i]}')






























