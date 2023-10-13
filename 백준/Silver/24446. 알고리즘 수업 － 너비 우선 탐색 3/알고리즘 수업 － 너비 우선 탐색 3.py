from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque([r])
    visited[r] = 0
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)
bfs(r)
for i in range(1, n + 1):
    print(visited[i])