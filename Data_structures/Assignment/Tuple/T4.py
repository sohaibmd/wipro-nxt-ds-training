#  4. Find the index of an item in a tuple

def index_in_tuple():
    tup = (10, 20, 30, 40, 50)
    item = int(input("Enter item to find index: "))
    if item in tup:
        print("Index of", item, "is", tup.index(item))
    else:
        print("Item not found in tuple.")

index_in_tuple()