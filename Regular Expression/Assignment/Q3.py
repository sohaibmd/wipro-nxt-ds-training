# Q3. Split irregular sentence into words

import re
sentence = '*""A, very very; irregular sentence"""'
cleaned = ' '.join(re.findall(r'\b\w+\b', sentence))
print(cleaned)
