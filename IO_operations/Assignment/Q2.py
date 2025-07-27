# 2. Read first n lines from a .txt file

def read_n_lines():
    filename = input("Enter the filename : ")
    n = int(input("Enter number of lines to read: "))
    try:
        with open(filename, 'r') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

read_n_lines()
