phonebook_dict = {}

while True:
    print('Выберите номер действия:')
    print('\t1. Добавить контакт')
    print('\t2. Найти человека')
    choice = int(input())
    if choice == 1:
        name_and_surname = input('Введите имя и фамилию нового контакта (через пробел): ').lower().split()
        name_and_surname = tuple(name_and_surname)
        if name_and_surname not in phonebook_dict:
            phonebook_dict[name_and_surname] = int(input('Введите номер: '))
        else:
            print('Такой контакт уже существует')
        print('Текущий словарь контактов:', phonebook_dict)
    elif choice == 2:
        surname = input('Введите фамилию для поиска: ').lower()
        for i_person, phone in phonebook_dict.items():
            if surname in i_person:
                print(i_person, phone)




