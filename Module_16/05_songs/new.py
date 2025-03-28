violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

def quantity_check():
    try:
        num_songs = int(input("Сколько песен выбрать? "))
        if 0 < num_songs <= len(violator_songs):
            return num_songs
        print(f"В альбоме только {len(violator_songs)} песен. Попробуйте снова.")
    except ValueError:
        print("Пожалуйста, введите целое число.")


def music_time():
    num = quantity_check()
    time = 0

    for i in range(num):
        while True:
            name_music = input(f"Введите название {i + 1}-й песни: ")
            song_found = False
            for lst in violator_songs:
                if name_music == lst[0]:
                    time += lst[1]
                    song_found = True
                    break

            if song_found:
                break
            else:
                print("Такой песни нет в альбоме. Попробуйте еще раз.")

    print(f"Общее время звучания песен: {round(time, 2)} минут")
    return time


if __name__ == "__main__":
    print(music_time())





