# 5. Dictionary with numbers 1 to 15 as keys and their squares as values

def squares_dictionary():
    square_dict = {x: x*x for x in range(1, 16)}
    print("Squares Dictionary:", square_dict)


squares_dictionary()