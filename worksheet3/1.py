def calculate_difference(number):
    if number > 17:
        return 2 * abs(number - 17)
    else:
        return abs(number - 17)

# Example usage
num = int(input("Enter a number: "))
print("Result:", calculate_difference(num))
