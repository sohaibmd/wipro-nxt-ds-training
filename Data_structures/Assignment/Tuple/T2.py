# 2. Check whether an element exists in a tuple

def check_element():
    tup = (10, 20, 30, 40, 50)
    element = int(input("Enter element to check: "))
    if element in tup:
        print(f"{element} exists in the tuple.")
    else:
        print(f"{element} does not exist in the tuple.")

check_element()