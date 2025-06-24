line_count = 0
sym_count = 0
error_message = []

try:
    with open('people.txt', 'r', encoding='utf-8') as people_file:
        for line_number, line in enumerate(people_file, 1):
            line = line.rsplit('\n')
            line_length = len(line[0])
            sym_count += line_length

            if line_length < 3:
                error = f'Ошибка: менее 3х символов в строке {line_number}, {line[0]}'
                print(error)
                error_message.append(error)

except FileNotFoundError:
    error = f"файл people.txt не найден"
    print(error)
    error_message.append(error)

finally:
    with open('errors.log', 'w', encoding='utf-8') as errors_file:
        for line in error_message:
            errors_file.write(f"{line} + \n")







