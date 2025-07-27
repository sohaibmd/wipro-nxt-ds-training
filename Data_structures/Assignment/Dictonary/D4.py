# 4. Iterate over dictionary and print keys, values, and both


def iterate_dictionary():
    my_dict = {1: 'a', 2: 'b', 3: 'c'}

    print("Keys:")
    for key in my_dict:
        print(key)

    print("Values:")
    for value in my_dict.values():
        print(value)

    print("Keys and Values:")
    for key, value in my_dict.items():
        print(f"{key} → {value}")

iterate_dictionary()