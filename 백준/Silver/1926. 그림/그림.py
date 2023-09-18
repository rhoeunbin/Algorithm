from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    each = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if pic[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    each += 1
    return each

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if pic[i][j] == 1 and not visited[i][j]:
            cnt += 1
            ans = max(bfs(i, j), ans)

print(cnt)
print(ans)