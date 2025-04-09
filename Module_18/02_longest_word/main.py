text = input('Введите строку: ').split()
count = []
for word in text:
    count.append(len(word))
print('Самое длинное слово:', max(text, key=len))
print('Длина этого слова:', max(count))
