def cesar_cipher(word, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ')for sym in word]
    new_str = ''
    for i_elem in char_list:
        new_str += i_elem
    return new_str

word = input('Введите слово или фразу: ')
shift = int(input('Введите сдвиг: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

output = cesar_cipher(word, shift)

print('Зашифрованная строка: ', output)