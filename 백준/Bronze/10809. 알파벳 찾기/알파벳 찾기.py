alpha = 'abcdefghijklmnopqrstuvwxyz'
s = input()
for i in alpha:
    if i in s:
        print(s.index(i), end = ' ')
    else:
        print(-1, end = ' ')