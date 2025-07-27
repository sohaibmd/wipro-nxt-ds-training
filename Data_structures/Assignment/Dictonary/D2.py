#  2. Concatenate multiple dictionaries into one

def concatenate_dicts():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    
    combined_dict = {}
    for d in (dic1, dic2, dic3):
        combined_dict.update(d)
    
    print("Concatenated Dictionary:", combined_dict)


concatenate_dicts()