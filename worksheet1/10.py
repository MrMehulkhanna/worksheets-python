year = int(input("Enter a year: "))\nif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n    print("The year is a leap year.")\nelse:\n    print("The year is not a leap year.")
