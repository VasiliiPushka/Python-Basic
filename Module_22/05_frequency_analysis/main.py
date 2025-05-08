line = 'Mama myla ramu.'
file = open('text.txt', 'w')
file.write(line)
file.close()

def statistics(file_name):
    result = {}
    count = 0
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for j_char in i_line.lower():
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
                count += 1
    text_file.close()
    analysis_file = open('analysis.txt ', 'w')
    for keys, values in result.items():
        analysis_file.write(str(keys) + ' ' + str(round(values / count, 3)) + '\n')
    analysis_file.close()
    return analysis_file



statistics('text.txt')
file = open('analysis.txt ', 'r')
print('Содержимое файла analysis.txt:')
for i_line in file:
    print(i_line.rstrip())