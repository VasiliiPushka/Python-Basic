string = input('Введите строку: ')
new_string = []
i_sym = 0
sym_count = 1
while i_sym < (len(string) - 1):
    if string[i_sym] == string[i_sym + 1]:
        sym_count += 1
    else:
        new_string.append(''.join([string[i_sym], str(sym_count)]))
        sym_count = 1
    i_sym += 1
string = [i for i in string]

for i in new_string:
    print(i, end='')





