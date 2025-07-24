# 5. Repeat last n characters n times 

def repeat_last_n_chars():
    s = input("Enter a string: ")
    n = int(input("Enter a number (between 1 and length of string): "))
    if 1 <= n <= len(s):
        last_n = s[-n:]
        result = last_n * n
        print("Output:", result)
    else:
        print("Invalid input.")

repeat_last_n_chars()