def n_gram(text,n):
    ans = []
    for i in range(len(text)-n+1):
        ans.append(text[i:i+n])
        return ans

text1 = "paraparaparadise"
text2 = "paragraph"

X = set(n_gram(text1,2))
Y = set(n_gram(text2,2))

print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合:", X - Y)

if "se" in X | Y:
    print("含まれる")
else:
    print("含まれない")