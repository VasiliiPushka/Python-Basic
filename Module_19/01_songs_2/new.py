violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

def sing_total_time():
    sings = int(input("Сколько песен выбрать? "))
    total_time = 0
    for i in range(sings):
        song = input(f"Название {i+1}-й песни: ")
        if song in violator_songs.keys():
            total_time += violator_songs.get(song)
        else:
            print("Песня отсутствует в альбоме")

    print(f"Общее время звучания песен: {round(total_time, 2)} минуты")


if __name__ == "__main__":
    sing_total_time()