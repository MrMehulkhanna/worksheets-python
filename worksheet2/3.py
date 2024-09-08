def multiply_list(lst):
    product = 1
    for item in lst:
        product *= item
    return product

lst = [1, 2, 3, 4, 5]
print("Product of list items:", multiply_list(lst))
