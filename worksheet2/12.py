list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

new_list = [x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 == 0]
print("New list:", new_list)
