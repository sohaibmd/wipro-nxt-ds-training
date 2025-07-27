# 4. List Index Access with Exception Handling

def check_list_index():
    numbers = [5, -2, 10, 0, -4, 3, -6, 8, -9, 1]
    try:
        index = int(input("Enter an index (0 to 9): "))
        value = numbers[index]
        if value >= 0:
            print(f"Number at index {index} is positive.")
        else:
            print(f"Number at index {index} is negative.")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer.")

check_list_index()