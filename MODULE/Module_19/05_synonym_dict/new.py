# few_word = int(input("Введите количество пар слов: "))
# synonyms = dict()
#
# for i in range(few_word):
#     word = input(f"{i+1}-я пара: ").lower().split(' - ')
#     synonyms[word[0]] = word[1]
#
# def check_word(string:str) -> bool:
#     if string in synonyms:
#         return True
#     elif string in synonyms.values():
#         return True
#     else:
#         return False
#
# flag = False
#
# while not flag:
#     word = input("Введите слово: ")
#     result = check_word(word)
#     if result:
#         for key, value in synonyms.items():
#             if key == word:
#                 print(f"Cиноним - {value}")
#                 flag = True
#                 break
#             else:
#                 print(f"Cиноним - {key}")
#                 flag = True
#                 break
#     else:
#         print("Такого слова в словаре нет.")


# Ввод словаря синонимов
synonyms = {}
for i in range(int(input("Введите количество пар слов: "))):
    pair = input(f"{i+1}-я пара: ").lower().split(' - ')
    synonyms[pair[0]] = pair[1]
    synonyms[pair[1]] = pair[0]  # Добавляем обратную связь для быстрого поиска

# Поиск синонима
while True:
    word = input("Введите слово: ").lower()
    if word in synonyms:
        print(f"Синоним - {synonyms[word]}")
        break
    print("Такого слова в словаре нет.")



