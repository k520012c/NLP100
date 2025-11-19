import re
section = r"\=\=\=+(.*?)\=\=\=+"

with open('20.txt', 'r') as f:
    for line in f:
        section_name = re.findall(section, line)
        level = int(line.count('=') / 2) - 1
        if section_name:
            print(f"{section_name}Level:{level}")