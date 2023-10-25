from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, 0] # 오른쪽
dy = [0, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        step = graph[x][y]
        if graph[x][y] == -1:
            print('HaruHaru')
            return
        for m in range(2):
            nx = x + dx[m]*step
            ny = y + dy[m]*step
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    print('Hing')
bfs(0, 0)