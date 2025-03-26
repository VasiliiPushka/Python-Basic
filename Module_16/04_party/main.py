guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    print('Гость пришел или ушел?', end=' ')
    choice = input()
    if choice == 'пришел' and len(guests) < 6:
        new_people = input('Имя гостя: ')
        print('Привет', new_people + '!')
        guests.append(new_people)
    elif choice == 'пришел' and len(guests) >= 6:
        new_people = input('Имя гостя: ')
        print('Прости', new_people, 'но мест нет')
    elif choice == 'ушел':
        del_people = input('Имя гостя: ')
        print('Пока', del_people)
        guests.remove(del_people)
    elif choice == 'Пора спать':
        break
print('\nВечеринка закончилась, все легли спать.')


