# 4. Remove 'x' if it is the first or last character

def remove_x_from_ends():
    s = input("Enter a string: ")
    if s.startswith('x'):
        s = s[1:]
    if s.endswith('x'):
        s = s[:-1]
    print("Output:", s)

remove_x_from_ends()