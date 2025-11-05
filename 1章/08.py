def cipher(lst):
    for i in range(len(lst)):
      if lst[i].islower() and lst[i].isalpha():
        lst[i] = chr(219 - ord(lst[i]))
    return lst

text = "4D3r4qryK89ru4q"
code= cipher(list(text))
print("暗号化:","".join(code))
print("複合化:","".join(cipher(code)))