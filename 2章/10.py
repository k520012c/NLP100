count = 0
with open('popular-names.txt') as f:
    for line in f:
        count += 1
print(count)

# wc <ファイル名>　で行数、文字数、単語数を確認できる