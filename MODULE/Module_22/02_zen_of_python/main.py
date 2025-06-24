file = open('zen.txt', 'r')
text_list = []
for i_str in file:
    text_list.append(i_str)
for i_str in text_list[::-1]:
    print(i_str.rstrip())
file.close()
