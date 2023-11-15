n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

arr = [[0] * k for _ in range(n)]

for i in range(n):
    res = []
    for l in range(k):
        ans = 0
        for j in range(m):
            ans += a[i][j] * b[j][l]
        res.append(ans)
    print(*res)