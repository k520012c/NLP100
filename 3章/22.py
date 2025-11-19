import re
category = r"\[\[Category:(.*?)\]\]"

with open('20.txt', 'r') as f:
    for line in f:
        category_name = re.findall(category, line)
        if category_name:
            print(category_name)