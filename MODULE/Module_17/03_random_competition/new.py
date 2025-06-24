import random

first_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
res_list = [first_list[i] if first_list[i] > second_list[i] else second_list[i]
            for i in range(20)]

print(f"{first_list}\n"
      f"{second_list}\n"
      f"{res_list}")