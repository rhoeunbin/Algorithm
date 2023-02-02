import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            dfs(x + dx[i], y + dy[i])
        return True

answer = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)

            answer += 1

print(answer)