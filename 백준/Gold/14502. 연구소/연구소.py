import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1 # 처음 0의 개수
max_res = 0

def bfs():
    visited = [[0] * m for _ in range(n)]
    global max_res
    # print(graph)
    res = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                visited[i][j] = 1
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <=ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    res += 1
                    q.append((nx,ny))           
    max_res = max(max_res, cnt - res)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0
wall(0)
print(max_res - 3)