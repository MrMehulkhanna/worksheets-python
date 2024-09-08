import random
import string

for _ in range(100):
    length = random.randint(6, 8)
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    print(random_string)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in range(600, 801):
    if is_prime(number):
        print(number, end=' ')
print()

for number in range(100, 1001):
    if number % 7 == 0 and number % 9 == 0:
        print(number, end=' ')
print()
