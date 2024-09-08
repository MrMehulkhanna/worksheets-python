L = [11, 12, 13, 14]

L.append(50)
L.append(60)
print("After adding 50 and 60:", L)

L.remove(11)
L.remove(13)
print("After removing 11 and 13:", L)

L.sort()
print("Sorted in ascending order:", L)

L.sort(reverse=True)
print("Sorted in descending order:", L)

print("13 is in L:", 13 in L)

print("Number of elements in L:", len(L))

print("Sum of elements in L:", sum(L))

odd_sum = sum(x for x in L if x % 2 != 0)
print("Sum of odd numbers in L:", odd_sum)

even_sum = sum(x for x in L if x % 2 == 0)
print("Sum of even numbers in L:", even_sum)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = sum(x for x in L if is_prime(x))
print("Sum of prime numbers in L:", prime_sum)

L.clear()
print("L after clearing:", L)

del L
