s = input()
for i in range(int(input())):
    a, l, r = input().split()
    ans = 0
    for j in range(int(l), int(r) + 1):
        if s[j] == a:
            ans += 1
    print(ans)