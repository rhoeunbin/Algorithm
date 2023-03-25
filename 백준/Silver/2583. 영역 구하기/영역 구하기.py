import sys
sys.setrecursionlimit(10000)

m, n, k = map(int,input().split())
graph = [[0] * n for _ in range(m)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(k):
    x, y, rx, ry = map(int,input().split())
    for i in range(y, ry):
      for j in range(x, rx):
          graph[i][j] = 1

def dfs(x, y, cnt):
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not graph[nx][ny]:
            cnt = dfs(nx, ny, cnt + 1)
    return cnt

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(dfs(i, j, 1))

print(len(result))
print(*sorted(result))
