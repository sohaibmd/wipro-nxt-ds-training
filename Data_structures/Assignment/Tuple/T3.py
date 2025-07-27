# 3. Convert a list into a tuple

def list_to_tuple():
    lst = input("Enter list elements separated by space: ").split()
    tpl = tuple(lst)
    print("Converted tuple:", tpl)

list_to_tuple()