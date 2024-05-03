t = int(input())

for _ in range(t):
    n, s = input().split()
    for i in range(len(s)):
        print(int(n)*s[i], end = '')
    print()