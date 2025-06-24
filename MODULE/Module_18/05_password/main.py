count_A = 0
count_a = 0
count_num = 0

while True:
    password = input('Придумайте пароль: ')
    for symbol in password:
        if symbol.islower() == True:
            count_a += 1
        if symbol.isupper() == True:
            count_A += 1
        if symbol.isdigit() == True:
            count_num += 1
    if len(password) < 8:
        print('Пароль ненадежный. Попробуйте еще раз')
    elif count_A < 1:
        print('Пароль ненадежный. Попробуйте еще раз')
    elif count_num < 3:
        print('Пароль ненадежный. Попробуйте еще раз')
    else:
        break
print('Это надежный пароль!')