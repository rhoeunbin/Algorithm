from collections import deque
import sys
input = sys.stdin.readline

c = int(input())
n = int(input())

arr = [[] for _ in range(c + 1)]
visited = [False] * (c + 1)
cnt = 0

for _ in range(n):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

def dfs(v):
    visited[v] = True
    global cnt
    for i in arr[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)
