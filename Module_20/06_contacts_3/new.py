phone_book = dict()

while True:
    choice = int(input(f"Введите номер действия: \n"
                       f" 1. Добавить контакт\n"
                       f" 2. Найти человека\n"
                       f"")
                 )

    if choice == 1:
        name_surname = input("Введите имя и фамилию нового контакта (через пробел): ").lower().split()
        name_surname = tuple(name_surname)
        if name_surname not in phone_book:
            phone_book[name_surname] = int(input("Введите номер: "))
        else:
            print("Такой контакт уже существует")
    elif choice == 2:
        surname = input("Введите фамилию для поиска: ").lower()
        for person, phone_num in phone_book.items():
            if surname in person:
                print(person, phone_num)








