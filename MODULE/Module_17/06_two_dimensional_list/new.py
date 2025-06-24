result_list = [[1, 5, 9],
               [2, 6, 10],
               [3, 7, 11],
               [4, 8, 12]]

start = 1
stop = 10
step = 4
res_list = [[i for i in range(start, stop, step)], [i for i in range(start+1, stop+1, step)],
               [i for i in range(start+2, stop+2, step)], [i for i in range(start+3, stop+3, step)]]
print(res_list)


