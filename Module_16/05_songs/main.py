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
song_time = []
total_time = 0

song_quantity = int(input('Сколько песен выбрать? '))
for num in range(song_quantity):
    print('Название', num + 1, '-й песни', end=': ')
    num = input()
    for song in violator_songs:
        if song[0] == num:
            song_time.append(song[1])

for time in song_time:
    total_time += time

print('Общее время звучания песен:', total_time)






