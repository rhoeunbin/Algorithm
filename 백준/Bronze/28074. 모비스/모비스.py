word = input()

for i in "MOBIS":
    if i not in word:
        print('NO')
        break
else:
    print('YES')