#  3. Check if a key exists in a dictionary

def check_key_exists():
    my_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}
    key = int(input("Enter key to check: "))
    
    if key in my_dict:
        print(f"Yes, key {key} exists.")
    else:
        print(f"No, key {key} does not exist.")

check_key_exists()