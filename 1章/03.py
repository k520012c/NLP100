a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text = a.replace(".", "").replace(",", "")
ans = []

for word in text.split():
    ans.append(len(word))
print(ans)