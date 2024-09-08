D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}

D[8] = 8.8
print("After adding new entry:", D)

del D[2]
print("After removing key 2:", D)

print("Key 6 is in D:", 6 in D)

print("Number of elements in D:", len(D))

value_sum = sum(D.values())
print("Sum of all values in D:", value_sum)

D[3] = 7.1
print("After updating key 3:", D)

D.clear()
print("D after clearing:", D)
