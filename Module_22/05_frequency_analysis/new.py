text = 'Mama myla ramu.'




def frequency_analysis():
    with open('text.txt', 'r', encoding='utf-8') as file:
        data = [sym for word in file for sym in word]

        dict_word = dict()

        for sym in data:
            if sym not in dict_word and sym.isalpha():
                dict_word[sym.lower()] = 1
            elif sym.isalpha():
                dict_word[sym.lower()] += 1
            else:
                continue

    return dict_word


def good_print(dictionary: dict):
    count_value = sum(dictionary.values())

    with open('analysis_2.txt', 'w', encoding='utf-8') as file:
        for key, value in dictionary.items():
            file.write(f"{key} {round(value / count_value, 3)}\n")

    return file


dictionary = frequency_analysis()
print(dictionary)

good_print(dictionary)
