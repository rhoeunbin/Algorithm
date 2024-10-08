c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
for i in c:
    word = word.replace(i, '@')
print(len(word))