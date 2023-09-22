from collections import deque
n, m, r = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)


def bfs(s):
    global cnt
    q = deque([s])
    visited[s] = 1
    while q:
        now = q.popleft()
        arr[now].sort()
        for i in arr[now]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                q.append(i)
bfs(r)   

for v in visited[1:]:
    print(v)