from collections import deque
import sys
input = sys.stdin.readline

def bfs(now):
    q = deque()
    q.append(now)

    while q:
        v = q.popleft()
        for n in graph[v]:
                if visited[n] == 0:
                    visited[n] = v
                    q.append(n)

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
visited = [False] * (n + 1)

bfs(1)
for i in range(2, n + 1):
    print(visited[i])