numbers = input("Enter comma-separated numbers: ").split(",")
num_list = [int(num) for num in numbers]
num_tuple = tuple(num_list)
print("List:", num_list)
print("Tuple:", num_tuple)
