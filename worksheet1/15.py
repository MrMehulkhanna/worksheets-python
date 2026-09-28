n = int(input("Enter a positive integer N: "))
sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
print("The sum of squares from 1 to", n, "is:", sum_of_squares)
