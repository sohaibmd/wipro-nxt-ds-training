#  1. Remove a given item from the set

def remove_item_from_set():
    s = set(input("Enter set elements separated by space: ").split())
    item = input("Enter item to remove: ")
    if item in s:
        s.remove(item)
        print("Updated set after removal:", s)
    else:
        print(f"Item '{item}' not found in set.")


remove_item_from_set()