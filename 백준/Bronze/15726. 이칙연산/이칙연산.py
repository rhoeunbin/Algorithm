a, b, c = map(int, input().split())

f = a*b/c
s = a/b*c

if f > s:
    print(int(f))
else:
    print(int(s))