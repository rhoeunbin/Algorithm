n = int(input())
find = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = -1, 0
d = -1
cnt = n ** 2


graph = [[0] * n for _ in range(n)] + [[0, 0]]
for _ in range(2 * n - 1):

    d = (d + 1) % 4
    for _ in range(n):
        x += dx[d]
        y += dy[d]

        graph[x][y] = cnt

        if cnt == find:
            graph[-1][0] = x + 1
            graph[-1][1] = y + 1
        cnt -= 1

    if not d or not d % 2:
        n -= 1

for i in graph:
    print(*i)