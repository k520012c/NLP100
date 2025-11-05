a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text = a.replace(".","").split()
ans = {}

for i,word in enumerate(text, 0):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        x = word[0]
        ans[x] = i+1

    else:
        x = word[:2]
        ans[x] = i+1
print(ans)