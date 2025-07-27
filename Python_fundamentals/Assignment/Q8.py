# Q8. Write a program to print the sum of all the digits of a given number.
num = int(input("Enter a number: "))
sum_digits = 0
temp = abs(num)

while temp > 0:
    sum_digits += temp % 10
    temp //= 10

print("Sum of digits:", sum_digits)
