films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
         'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

def good_films() -> str:
    love_films = []
    num_films = int(input('Number of movies you want to add? - '))
    for num in range(num_films):
        film = input('Enter the movie name: ')
        if film in films:
            love_films.append(film)
        else:
            print(f"Error: we don't have the movie {film}")
    return f"Your list of favorite movies: {love_films.}"


if __name__ == "__main__":
    print(good_films())
