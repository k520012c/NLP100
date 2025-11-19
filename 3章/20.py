import json

output_path = '20.txt'

with open('jawiki-country.json', 'r') as f:
    for line in f:
        article = json.loads(line)
        if article["title"] == "イギリス":
            print(article["text"])
            break

with open(output_path, 'w') as out:
    out.write(article["text"])