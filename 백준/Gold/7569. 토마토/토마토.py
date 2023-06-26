from collections import deque

m, n, h = map(int, input().split())
graph = []
q = deque()

for i in range(h):
    info = []
    for j in range(n):
        info.append(list(map(int, input().split())))
        for k in range(m):
            if info[j][k] == 1:
                q.append((i, j, k))
    graph.append(info)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny <n and 0 <= nz < m and graph[nx][ny][nz] == 0:
                q.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1

bfs()

ans = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))
print(ans - 1)