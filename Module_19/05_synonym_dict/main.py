quantyty = int(input('Введите кол-во пар слов: '))
word_list = []
word_dict = {}
for n in range(quantyty):
    word = input(f'{n+1}я пара: ').lower().split()
    word_list.append(word)

for word in word_list:
    word_dict[word[0]] = word[2]

while True:
    string = input('Введите слово: ').lower()
    key = ''
    i_values = ''
    for key, i_values in word_dict.items():
        if key == string:
            print(f'Синоним: {word_dict.get(key)}')
            break
        elif i_values == string:
            print(f'Синоним: {key}')
            break
    if key != string and i_values != string:
        print('Такого слова в словаре нет.')
    else:
        break


















