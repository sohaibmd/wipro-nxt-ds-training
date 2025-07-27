# Q1. Check if strings are valid octal numbers

import re

data = ['789', '123', '004']
result = [s for s in data if re.fullmatch(r'[0-7]+', s)]
print("Valid octal strings:", result)
