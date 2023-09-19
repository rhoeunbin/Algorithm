from collections import deque
def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True
    cnt = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt

t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for i in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(bfs(1))