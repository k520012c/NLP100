N = 10
with open('popular-names.txt') as f:
     for i, line in enumerate(f):
        if i >= N:
            break
        print(line, end='')

# head -n <ファイル名> でファイルの最初のn行を確認できる