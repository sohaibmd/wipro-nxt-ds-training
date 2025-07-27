# Q10. Write a program to find if the given number is palindrom or not.

num = int(input("Enter a number: "))
original = str(num)
reversed_num = original[::-1]

if original == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")
