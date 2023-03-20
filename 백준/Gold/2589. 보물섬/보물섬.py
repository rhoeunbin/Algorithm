from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx, ny))
    return cnt-1

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            ans = max(ans, bfs(i, j))
print(ans)