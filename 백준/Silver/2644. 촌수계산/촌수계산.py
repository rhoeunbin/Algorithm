from collections import deque

n = int(input())
o, t = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)

bfs(o)
if visited[t] > 0:
    print(visited[t])
else:
    print(-1)