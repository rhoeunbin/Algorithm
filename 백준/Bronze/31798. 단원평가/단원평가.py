a, b, c = map(int, input().split())

if a == 0:
    print(int(c**2 - b))
elif b == 0:
    print(int(c**2 - a))
else:
    print(int((a + b) ** (1 / 2)))