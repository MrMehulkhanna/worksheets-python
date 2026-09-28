principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))
compoundings_per_year = int(input("Enter the number of times interest is compounded per year: "))
amount = principal * (1 + rate / (100 * compoundings_per_year)) ** (compoundings_per_year * time)
interest = amount - principal
print("The compound interest is:", interest)
