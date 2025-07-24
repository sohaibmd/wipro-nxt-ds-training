#  2. Create an intersection of two sets

def intersection_of_sets():
    set1 = set(input("Enter first set elements: ").split())
    set2 = set(input("Enter second set elements: ").split())
    inter = set1 & set2
    print("Intersection:", inter)

intersection_of_sets()