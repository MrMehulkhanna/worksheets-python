numbers = input("Enter comma-separated numbers: ").split(",")\nnum_list = [int(num) for num in numbers]\nnum_tuple = tuple(num_list)\nprint("List:", num_list)\nprint("Tuple:", num_tuple)
