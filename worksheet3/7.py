def outer_function():
    def inner_function():
        return "Hello from inner function!"
    
    result = inner_function()
    print(result)

# Example usage
outer_function()
