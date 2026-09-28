n = int(input("Enter a positive integer: "))
if n > 1:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")
else:
    print("The number is not prime.")
