#  3. Read File and Print Contents in Title Case

def read_file_title_case():
    filename = input("Enter the filename (with .txt): ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Content in Title Case:\n")
            print(content.title())
    except FileNotFoundError:
        print("Error: File not found.")

read_file_title_case()