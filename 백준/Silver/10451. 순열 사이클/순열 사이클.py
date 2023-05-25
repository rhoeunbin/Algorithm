import sys
sys.setrecursionlimit(1000)

def dfs(v):
    visited[v] = True
    next = num[v]
    if not visited[next]:
        dfs(next)

for _ in range(int(input())):
    n = int(input())
    num = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            result += 1 
    print(result)