# 2. Check whether a string is palindrome or not

def is_palindrome():
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")

is_palindrome()