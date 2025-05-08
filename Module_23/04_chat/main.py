user_name = input('как вас зовут? ')
while True:
    print('Чтобы видеть текущий текст чата введите 1, чтобы написать сообщение введите 2')
    response = input('Введите 1 или 2: ')
    if response == '1':
        try:
            with open('chat.txt', 'r') as file:
                massages = file.readlines()
                print(''.join(massages))
        except FileNotFoundError:
            print('Служебное сообщение: пока ничего нет\n')
    elif response == '2':
        new_massage = input('Введите сообщение: ')
        with open('chat.txt', 'a') as file:
            file.write('{name}: {massage}\n'.format(
                name=user_name, massage=new_massage))
    else:
        print('Неизвестная команда\n')

