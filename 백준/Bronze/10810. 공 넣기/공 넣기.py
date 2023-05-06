n, m = map(int, input().split())
b = [0] * (n + 1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j + 1):
        b[x] = k

for i in range(n):
    print(b[i + 1], end = ' ')