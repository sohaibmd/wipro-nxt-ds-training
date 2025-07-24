#  5. Function to print even numbers from a list

def even_numbers(lst):
    evens = [num for num in lst if num % 2 == 0]
    return evens

# Sample test
print("Even numbers:", even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [2, 4, 6, 8]
