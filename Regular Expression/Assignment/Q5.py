# Q5. Extract text between HTML tags

import requests # type: ignore
import re

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text

# Extract text between tags
results = re.findall(r'>([^<>]+)<', html)
results = [text.strip() for text in results if text.strip()]
print(results)
