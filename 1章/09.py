import random
text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = text.split()

def change(word):
    if len(word) > 4:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + "".join(middle) + word[-1]
    else:
        return word

for i in range(len(words)):
    (words[i]) = change(words[i])

print(" ".join(words))