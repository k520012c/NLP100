from collections import Counter

count = Counter()
with open('popular-names.txt') as f:
    for line in f:
        name = line.split('\t')[0]
        count.update([name])
        
for name, cnt in count.most_common():
     print(f"{cnt} {name}")


#cut -f1 popular-names.txt | sort | uniq -c | sort -nr 
