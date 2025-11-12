N = 10 
with open('popular-names.txt') as f: 
    lines = f.readlines()
    for line in lines[-N:]:
        print(line,end="")

# tail -n <ファイル名> でファイルの最後のn行を確認できる