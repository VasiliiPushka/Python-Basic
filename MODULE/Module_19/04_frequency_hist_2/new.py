def histogram(string:str):
    sym_dict = dict()
    for sym in string:
        if sym not in sym_dict.keys():
            sym_dict[sym] = 1
        else:
            sym_dict[sym] += 1
    return sym_dict

def reverse_histogram(string):
    new_dict = dict()
    for key in string.keys():
        if string[key] not in new_dict:
            new_dict[string[key]] = [key]
        else:
            new_dict[string[key]].append(key)
    return new_dict



if __name__ == "__main__":
    res = histogram('здесь что-то написано')
    print(reverse_histogram(res))
