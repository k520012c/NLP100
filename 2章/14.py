N = 10 
with open('popular-names.txt') as f:
    line = f.readlines()
    for line in line[:N]:
        print(line[0])

#cut -c n <ファイル名> でn列目の文字を取り出す