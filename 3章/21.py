import re
category = r"\[\[Category:(.*?)\]\]"

with open('20.txt', 'r') as f:
    for line in f:
        if re.search(category, line):
            print(line.strip())