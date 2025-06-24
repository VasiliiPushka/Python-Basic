from typing import List

# Примеры списков:
letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

letter_num_list: List[tuple] = list(map(lambda x, y: (x, y), letters, numbers))
print(letter_num_list)