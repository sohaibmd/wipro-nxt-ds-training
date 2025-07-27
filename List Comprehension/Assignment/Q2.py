# Q2. Dictionary of 26 alphabets with corresponding integer

import string

alphabet_dict = {char: idx + 1 for idx, char in enumerate(string.ascii_lowercase)}
print(alphabet_dict)
