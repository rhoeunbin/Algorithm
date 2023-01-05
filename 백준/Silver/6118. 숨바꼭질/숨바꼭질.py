from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            # if not visited[i]:
            #     visited[i] = visited[v] + 1
            #     queue.append(i)
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)

N, M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [0] * (N + 1)
bfs(1)
m_visit = max(visited)

print(visited.index(m_visit), m_visit-1, visited.count(m_visit))