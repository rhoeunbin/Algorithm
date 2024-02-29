from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    s, e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

for i in range(n + 1):
    arr[i].sort()

def dfs(v):
    print(v, end = ' ')
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end = ' ')
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

dfs(start)
print()
visited = [False] * (n + 1)
bfs(start)