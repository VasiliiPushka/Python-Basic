import functools
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

sort_floats: List[float] = list(map(lambda elem: round(elem**3, 3), floats))
print(sort_floats)

sort_names: List[str] = list(filter(lambda name: len(name) >= 5, names))
print(sort_names)

sort_numbers = functools.reduce(lambda a, b: a*b, numbers)
print(sort_numbers)
