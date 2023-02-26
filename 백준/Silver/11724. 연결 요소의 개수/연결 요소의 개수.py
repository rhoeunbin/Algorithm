from collections import deque
import sys
input = sys.stdin.readline

def bfs(v, graph, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        now = queue.popleft()

        for j in graph[now]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
visited = [False]*(n+1)

for i in range(1, n+1):
    if not visited[i]:
        result += 1
        bfs(i, graph, visited)
print(result)
