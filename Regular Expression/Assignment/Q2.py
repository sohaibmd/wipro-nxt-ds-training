# Q2. Extract user id, domain name, and suffix from email
import re
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

matches = re.findall(r'([\w\d]+)@([\w\d]+)\.([\w]+)', emails)
for m in matches:
    print(f"User: {m[0]}, Domain: {m[1]}, Suffix: {m[2]}")
