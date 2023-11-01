def bfs():
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return graph[x][y]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not graph[nx][ny]:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    graph = [[0] * l for _ in range(l)]
    print(bfs())
