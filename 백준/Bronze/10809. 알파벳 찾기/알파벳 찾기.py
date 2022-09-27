s = input()
word =  'abcdefghijklmnopqrstuvwxyz'

for i in word:
    if i in s:
        print(s.index(i), end = ' ')
    else:
        print(-1, end = ' ')