import random

with open('popular-names.txt') as f:
    lines = f.readlines() 

random.shuffle(lines)

for line in lines:
    print(line, end='')


#shuf <ファイル名> で行をランダムに表示する
