nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [sym for list_1 in nice_list
          for list_2 in list_1
          for sym in list_2]
print(result)