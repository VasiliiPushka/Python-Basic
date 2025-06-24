def height_sort(my_list):
    for i_mn in range(len(my_list)):
        for height_people in range(i_mn, len(my_list)):
            if my_list[height_people] < my_list[i_mn]:
                my_list[height_people], my_list[i_mn] = my_list[i_mn], my_list[height_people]
    print(my_list)

sort_class = []
first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))
print(first_class)
print(second_class)

first_class.extend(second_class)
height_sort(first_class)


