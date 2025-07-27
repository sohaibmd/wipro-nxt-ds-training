# 2. Check Prime with Input Validation

def check_prime():
    try:
        n = int(input("Enter a number: "))
        if n <= 1:
            print("Not a prime number.")
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    print("Not a prime number.")
                    return
            print("It is a prime number.")
    except ValueError:
        print("Error: Please enter a valid number.")

check_prime()