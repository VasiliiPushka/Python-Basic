file_number = open('numbers.txt', 'r', encoding='utf-8')
file_answer = open('answer.txt', 'w', encoding='utf-8')
count = 0

number_tuple = (int(sym) for string in file_number for sym in string.strip())
for num in number_tuple:
    count += num

file_answer.write(str(count))
file_number.close()
file_answer.close()