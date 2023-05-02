n, q = map(int, input().split())
num = list(map(int, input().split()))
res = 0

for _ in range(q):
    i, j = map(int, input().split())
    if j - 1 < i:
        print(0)
    else:
        ans = 0
        for x in range(i - 1, j - 1):
            ans += abs(num[x] - num[x + 1])
        print(ans)