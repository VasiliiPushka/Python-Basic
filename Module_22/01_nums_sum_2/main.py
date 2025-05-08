
summ_number = []
file = open('numbers.txt', 'r')
for i_line in file:
    summ_number.append(i_line.split())
file.close()
print(summ_number)
summ = 0
for i_elem in summ_number:
    for j_elem in i_elem:
        summ += int(j_elem)
print(summ)
file_2 = open('answer.txt', 'w')
file_2.write(str(summ))
file_2.close()

