def validation_string(string:str):
    try:
        string = string.split()
        if not string[0].isalpha():
            raise NameError ('Поле «Имя» содержит НЕ только буквы:')
        elif int(string[2]) > 99 or int(string[2]) < 10:
            raise ValueError ('Возраст» НЕ является числом от 10 до 99')
        elif '@' not in string[1] or '.' not in string[1]:
            raise SyntaxError ('«Имейл» НЕ содержит @ и . (точку)')
        elif len(string) < 3:
            raise IndexError ('НЕ присутствуют все три поля: IndexError')

        return True

    except NameError:
        print('Поле «Имя» содержит НЕ только буквы:')
        return False
    except ValueError:
        print('Возраст» НЕ является числом от 10 до 99')
        return False
    except SyntaxError:
        print('«Имейл» НЕ содержит @ и . (точку)')
        return False
    except IndexError:
        print('НЕ присутствуют все три поля: IndexError')
        return False


with (
    open('registrations.txt', 'r', encoding='utf-8') as read_file,
    open('registrations_good.log', 'a', encoding='utf-8') as good_file,
    open('registrations_bad.log', 'a', encoding='utf-8') as bad_file):
    for line in read_file:
        string = validation_string(line)
        if string is True:
            good_file.write(line)
        else:
            bad_file.write(line)









