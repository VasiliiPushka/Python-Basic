from collections import Counter


def count_unique_characters(string: str) -> int:
    uniq_symbols = sum(list(map(lambda x: x == 1, Counter(string).values())))
    return uniq_symbols


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
