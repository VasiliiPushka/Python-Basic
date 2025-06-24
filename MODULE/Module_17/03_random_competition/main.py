import random

first_com = [round(random.uniform(5, 10), 2) for i in range(20)]
second_com = [round(random.uniform(5, 10), 2) for j in range(20)]
result = []

print('Первая команда:', first_com)
print('Вторая команда:', second_com)

result = [(first_com[i_elem] if first_com[i_elem] - second_com[i_elem] > 0
           else second_com[i_elem])
          for i_elem in range(20)]

print('Победители тура:', result)
