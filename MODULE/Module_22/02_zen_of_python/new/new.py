file = open('zen.txt', 'r', encoding='utf-8')

list_zen = [string for string in file]
for string in list_zen[::-1]:
    print(string.strip('\n'))