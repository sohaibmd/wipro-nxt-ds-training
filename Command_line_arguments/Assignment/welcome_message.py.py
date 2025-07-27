# 2. Accept welcome message and display filename + message



import sys

if len(sys.argv) != 2:
    print("Usage: python welcome_message.py <welcome_message>")
else:
    print("File Name:", sys.argv[0])
    print("Welcome Message:", sys.argv[1])
 