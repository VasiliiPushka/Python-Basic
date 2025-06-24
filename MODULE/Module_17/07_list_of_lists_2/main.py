nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [i_elem for list1 in nice_list
          for list2 in list1
          for i_elem in list2]
print(result)

# new_list = []
# for i_elem in nice_list:
#     new_list.extend(i_elem)
# print(new_list)
#
# new_list1 = []
# for i_elem in new_list:
#     new_list1.extend(i_elem)
# print(new_list1)

# res_list = []
# total_list = []
# result = [res_list.extend(i_elem) for i_elem in nice_list]
# total = [total_list.extend(i_elem) for i_elem in res_list]
# print(total_list)
