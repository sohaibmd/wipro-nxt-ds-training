# Q3.Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

a = int(input("Enter first non-negative number: "))
b = int(input("Enter second non-negative number: "))

if a >= 0 and b >= 0:
    if a % 10 == b % 10:
        print("True")
    else:
        print("False")
else:
    print("Please enter non-negative numbers only.")
