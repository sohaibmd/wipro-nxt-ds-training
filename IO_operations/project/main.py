import re
from collections import Counter

def get_meeting_time(lines_count):
    if lines_count <= 12:
        return f"{lines_count} AM"
    else:
        return f"{lines_count - 12} PM"

def get_most_frequent_word(text):
    # Remove punctuation and convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common_word, _ = word_counts.most_common(1)[0]
    return most_common_word.capitalize()  # Capitalize for proper name

def decode_secret_message(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            text = ' '.join(lines)

            # Step 1: Get meeting time
            line_count = len(lines)
            meeting_time = get_meeting_time(line_count)

            # Step 2: Get meeting place
            most_frequent_word = get_most_frequent_word(text)
            meeting_place = f"{most_frequent_word} Street"

            # Output result
            print("Meeting time:", meeting_time)
            print("Meeting place:", meeting_place)

    except FileNotFoundError:
        print("File not found. Please check the filename and path.")

# Replace 'sample.txt' with the path of your actual file
decode_secret_message("IO_operations\project\sample.txt")
