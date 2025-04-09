from itertools import count

string = input("Введите слова через пробел: ")
print(f"Самое длинное слово: {max(string.split(), key=len)}"
      f"Длина этого слова: {len(max(string.split()))}")


