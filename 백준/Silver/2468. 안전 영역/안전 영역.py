import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
max_h = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] > max_h: # 최대 높이값 저장
            max_h = graph[i][j]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

ans = 0 # 결과값
for high in range(max_h):
    visited = [[0] * n for _ in range(n)]
    cnt = 0 # 안전영역 개수

    for i in range(n):
        for j in range(n):
            if graph[i][j] > high and visited[i][j] == 0:
                bfs(i, j, high)
                cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)