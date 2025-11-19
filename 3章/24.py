import re

pattern = r"\[\[ファイル:(.*?)(?:\||\])"

with open('20.txt', 'r') as f:
    for line in f:
        file = re.findall(pattern, line)
        if file:
            print(file)