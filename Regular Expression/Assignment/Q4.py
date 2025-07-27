#  Q4. Clean up tweet




import re

tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej@pxDd cc: @garybernhardt #rstats"

cleaned = re.sub(r'(RT|cc:)|@[A-Za-z0-9_]+|http\S+|#\S+|[^\w\s]', '', tweet)
print(' '.join(cleaned.split()))
