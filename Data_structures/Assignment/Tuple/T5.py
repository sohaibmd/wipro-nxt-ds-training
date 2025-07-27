#  5. Replace last value of each tuple in a list with 100

def replace_last_in_tuples():
    sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    updated_list = [t[:-1] + (100,) for t in sample_list]
    print("Updated list:", updated_list)

replace_last_in_tuples()