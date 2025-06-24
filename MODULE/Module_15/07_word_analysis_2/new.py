def check_palindrome() -> str:
    word = input('Enter a word: ')
    new_word = [i for i in word]
    r_list = new_word[::1]
    if new_word == r_list:
        return "the word is a palindrome"
    else:
        return "the word is not a palindrome"

if __name__ == "__main__":
    print(check_palindrome())