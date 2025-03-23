films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']# список доступных фильмов

user_films = []#фильмы, которые добавит пользователь

quantity = int(input('Сколько фильмов хотите добавить? '))
for _ in range(quantity):
    name = input('Введите название фильма: ')
    for name_film in films:
        if name_film == name:
            user_films.append(name)


print('Ваш список любимых фильмов:', end=' ')
for i in user_films:
    print(i, end=', ')

