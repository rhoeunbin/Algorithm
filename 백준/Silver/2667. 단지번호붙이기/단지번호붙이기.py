import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
ans = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    global cnt
    graph[x][y] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            cnt = 1
            bfs(x, y)
            ans.append(cnt)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])