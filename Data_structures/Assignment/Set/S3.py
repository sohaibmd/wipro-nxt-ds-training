# 3. Create a union of two sets

def union_of_sets():
    set1 = set(input("Enter first set elements: ").split())
    set2 = set(input("Enter second set elements: ").split())
    uni = set1 | set2
    print("Union:", uni)

union_of_sets()