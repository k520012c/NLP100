import numpy as np
N = 3
with open('popular-names.txt') as f:
    line = f.readlines()

splits = np.array_split(line, N)

for i, chunk in enumerate(splits):
    filename = f'popular-names-part{i+1}.txt'
    with open(filename, 'w') as out:
        out.writelines(chunk)

# split -1 n <ファイル名> でファイルをn分割する