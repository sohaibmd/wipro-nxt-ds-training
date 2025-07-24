#  1. Division with Exception Handling

def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid integers.")

divide_numbers()