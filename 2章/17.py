with open('popular-names.txt') as f:
    lines = f.readlines()
    column = set()
    for line in lines:
        columns = line.strip().split('\t')
        column.add (columns[0])

print(len(column))

#cut -fn popular-names.txt | sort | uniq でn行目の重複を削除し表示
        