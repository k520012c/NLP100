def n_gram(text,n):
    ans = []
    for i in range(len(text)-n+1):
        ans.append(text[i:i+n])
        return ans

text = "I am an NLPer"
word = text.replace(" ","")
print("tri-grams:", n_gram(word,3))

sentence = text.split()
print("bi-grams:", n_gram(sentence,2))