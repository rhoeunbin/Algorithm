from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(x):
    global cnt
    q = deque([r])
    visited[r] = 1
    while q:
        x = q.popleft()
        graph[x].sort(reverse=True)
        for i in graph[x]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                q.append(i)

bfs(r)
for i in range(1, n + 1):
    print(visited[i])