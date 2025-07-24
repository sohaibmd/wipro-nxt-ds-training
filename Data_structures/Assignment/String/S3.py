# 3. Return n copies of first 2 characters where n = length of string

def first2_repeat_n_times():
    s = input("Enter a string (length >= 2): ")
    if len(s) >= 2:
        result = s[:2] * len(s)
        print("Output:", result)
    else:
        print("String is too short.")

first2_repeat_n_times()