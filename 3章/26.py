import re

pattern_1 = r"(?<=基礎情報)(.*)(?=\n\}\}\n)"
pattern_2 = r"^\|([^=]+?)\s*=\s*(.*)"
dic={}

with open('20.txt', 'r') as f:
    text = f.read()

match = re.search(pattern_1, text, re.DOTALL)
if match:
    info_block = match.group(1)
    for line in info_block.split("\n"):
        m = re.match(pattern_2, line)
        if m:
            key = m.group(1).strip()
            value = re.sub(r"'{2,5}", "", m.group(2).strip())
            dic[key] = value


print(dic)