import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    global cnt
    visited[v] = cnt
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)
dfs(r)

for i in visited[1:]:
    print(i)