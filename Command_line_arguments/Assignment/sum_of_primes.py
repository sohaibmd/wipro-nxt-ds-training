#  3. Accept 10 numbers, calculate the sum of prime numbers

# sum_of_primes.py

import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Usage: python sum_of_primes.py <10 space-separated numbers>")
else:
    numbers = list(map(int, sys.argv[1:]))
    prime_sum = sum(n for n in numbers if is_prime(n))
    print("Sum of prime numbers:", prime_sum)
