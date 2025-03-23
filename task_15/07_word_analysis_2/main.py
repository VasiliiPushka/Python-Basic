
word = input('Введите слово: ')
word_list = list(word)
new_word_list =[]

for index in word_list:
    new_word_list.append(index)
new_word_list.reverse()
if word_list == new_word_list:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')


