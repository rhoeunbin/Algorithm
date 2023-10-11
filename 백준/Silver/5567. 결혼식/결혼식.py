from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    q = deque()
    visited[s] = 1
    q.append(s)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[x] + 1

bfs(1)
print(visited.count(2) + visited.count(3))