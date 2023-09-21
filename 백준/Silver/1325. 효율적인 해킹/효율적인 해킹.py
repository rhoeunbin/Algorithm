import sys
input = sys.stdin.readline
from collections import deque

n, m =  map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(v):
    cnt = 1
    q = deque([v])
    visited = [0] * (n + 1)
    visited[v] = 1
    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt

res = []
for i in range(1, n + 1):
    res.append(bfs(i))

ans = max(res)
for i in range(len(res)):
    if ans == res[i]:
        print(i + 1, end = ' ')
