N = 10 
with open('popular-names.txt') as f:
    line = f.readlines()
    for line in line[:N]:
        line = line.replace('/t',' ')
        print(line,end="")

#sed 's/置換したい文字列/置換する文字列/g' <ファイル名>　で置換可能