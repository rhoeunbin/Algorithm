word = ""

for i in input():
    if i.islower():
        word += i.upper()
    else:
        word += i.lower()
print(word)