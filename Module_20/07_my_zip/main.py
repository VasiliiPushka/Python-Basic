def shorted_seq_range(string, tuple):
    return min(len(string), len(tuple))

syms_str = 'abcd'
nums_tuple = (10, 20, 30, 40)

pairs = ((syms_str[i_elem], nums_tuple[i_elem])
    for i_elem in range(shorted_seq_range(syms_str, nums_tuple)))
print(pairs)
for i_elem in pairs:
    print(i_elem)
