#  3. Accept input from user and append it to a .txt file

def append_to_file():
    filename = input("Enter file name: ")
    user_input = input("Enter text to append: ")
    with open(filename, 'a') as file:
        file.write(user_input + '\n')
    print("Text appended successfully.")

append_to_file()