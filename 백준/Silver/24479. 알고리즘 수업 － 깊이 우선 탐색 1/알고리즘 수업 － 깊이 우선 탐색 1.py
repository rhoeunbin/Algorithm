def dfs(v):
    global cnt
    visited[v] = cnt
    arr[v].sort()
    for i in arr[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, r = map(int,input().split())
arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)
dfs(r)
for i in range(1, n + 1):
    print(visited[i])