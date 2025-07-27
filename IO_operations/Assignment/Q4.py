#  4. Read file line by line and store into a list

def file_lines_to_list():
    filename = input("Enter file name: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            print("List of lines:", lines)
    except FileNotFoundError:
        print("File not found.")

file_lines_to_list()