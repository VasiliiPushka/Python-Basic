def num_pass(string:str) -> bool:
    count = 0
    for sym in string:
        if sym.isdigit():
            count += 1
    if count >= 3: return True
    else: return False

def big_word(string:str) -> bool:
    count = 0
    for sym in string:
        if sym.isupper():
            count += 1
    if count >= 1: return True
    else: return False


while True:
    password = input("Придумайте пароль: ")
    if len(password) < 8:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
    elif num_pass(password) is False:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
    elif big_word(password) is False:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
    else:
        print("Это надёжный пароль!")








