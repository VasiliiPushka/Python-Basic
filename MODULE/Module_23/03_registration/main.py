with open('registrations.txt', 'r', encoding='utf-8') as file, \
     open('registrations_good.log', 'w', encoding='utf-8') as good_file, \
     open('registrations_bad.log', 'w', encoding='utf-8') as bad_file:
    for line in file:
        line = line.rstrip()
        check_list = line.split()
        try:
            if len(check_list) < 3:
                raise IndexError(f'{line} - НЕ присутствуют все три поля')
            if not check_list[0].isalpha():
                raise NameError(f'{line} - Поле «Имя» содержит НЕ только буквы')
            if '@' not in check_list[1] or '.' not in check_list[1]:
                raise SyntaxError(f'{line} - Поле «Имейл» НЕ содержит @ и точку')
            if not 10 <= int(check_list[2]) <=99:
                raise ValueError(f'{line} - Поле «Возраст» НЕ представляет число от 10 до 99')
        except (IndexError, NameError, SyntaxError, ValueError) as exception:
            bad_file.write(f'{exception}\n')
        else:
            good_file.write(f'{line}\n')




