# 3. Function to calculate factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print("Factorial:", factorial(5))  # Output: 120
