# Q7. Write a program to print prime numbers between 10 and 99.
for num in range(10, 100):
    is_prime = True
    if num < 2:
        continue
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
