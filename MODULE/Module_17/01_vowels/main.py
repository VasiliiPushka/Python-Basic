
text = input('Введите текст: ')
words = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
new_text = list(text.lower())
new_words = [i for i in new_text for j in words if i == j]
#print(new_text)
print(new_words)