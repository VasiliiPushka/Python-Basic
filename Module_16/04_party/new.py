guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

def dacha():
    while True:
        print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
        question = input("Гость пришел или ушел? - ").lower()
        if question == "пришел" and len(guests) < 6:
            guest_name = input("Введите имя гостя: ")
            guests.append(guest_name)
            print(f"Привет, {guest_name}")
        elif len(guests) == 6 and question == "пришел":
            guest_name = input("Введите имя гостя: ")
            print(f"Прости {guest_name}, но мест нет")
        elif question == "ушел" and len(guests) <= 6:
            guest_name = input("Введите имя гостя: ")
            guests.remove(guest_name)
            print(f"Пока {guest_name}")
        elif question == "пора спать":
            break
        elif len(guests) == 0:
            break

    print(f"Сейчас на вечеринке {len(guests)}\n"
          f"Пора спать")

if __name__ == "__main__":
    dacha()