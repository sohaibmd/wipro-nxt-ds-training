# 6. Count frequency of a user-entered word in a .txt file

def count_word_frequency():
    filename = input("Enter file name: ")
    search_word = input("Enter word to count: ").lower()
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            words = content.split()
            count = words.count(search_word)
            print(f"'{search_word}' occurred {count} time(s).")
    except FileNotFoundError:
        print("File not found.")

count_word_frequency()