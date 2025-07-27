# 5. Find the longest word from the file (assuming only one longest word)

def find_longest_word():
    filename = input("Enter file name: ")
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            longest = max(words, key=len)
            print("Longest word:", longest)
    except FileNotFoundError:
        print("File not found.")

find_longest_word()