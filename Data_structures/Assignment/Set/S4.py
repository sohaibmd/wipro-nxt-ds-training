#  4. Find max and min value in a set

def max_min_in_set():
    s = set(map(int, input("Enter numbers separated by space: ").split()))
    if s:
        print("Maximum:", max(s))
        print("Minimum:", min(s))
    else:
        print("Set is empty.")

max_min_in_set()