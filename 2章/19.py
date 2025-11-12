with open('popular-names.txt') as f:
    lines = f.readlines()

num = sorted(lines, key=lambda line: int(line.split('\t')[2]), reverse=True)

for line in num:
    print(line,end="")

# sort -k3,3nr popular-names.txt  