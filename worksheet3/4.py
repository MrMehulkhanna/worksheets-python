def count_case_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

# Example usage
string = input("Enter a string: ")
upper, lower = count_case_letters(string)
print("Upper case letters:", upper)
print("Lower case letters:", lower)
