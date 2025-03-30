def analysis_text(text:str) -> list[str]:
    vowels_letter = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
    new_text = text.lower()
    list_vowels_letter = [let for let in new_text for j in vowels_letter if let == j]
    return list_vowels_letter

if __name__ == "__main__":
    print(analysis_text('Нужно отнести кольцо в Мордор!'))