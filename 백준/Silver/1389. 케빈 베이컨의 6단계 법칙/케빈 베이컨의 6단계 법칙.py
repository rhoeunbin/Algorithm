import sys
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = True

    while q:
        t = q.popleft()
        for i in arr[t]:
            if not visited[i]:
                visited[i] = visited[t] + 1
                q.append(i)



n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
res = []

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i)
    res.append(sum(visited))

print(res.index(min(res)) + 1)