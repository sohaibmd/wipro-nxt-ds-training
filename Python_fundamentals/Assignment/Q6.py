# Q6. Write a program to check if a given number is prime or not.
num = int(input("Enter a number: "))
if num < 2:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
