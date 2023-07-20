from collections import deque

a, b, n, m = map(int,input().split())
# 첫 줄에 스카이 콩콩의 힘 a와 b, 그리고 동규의 현재위치 n(시작), 주미의 현재 위치 m(끝)
graph = [False] * 100001

def bfs(v):
    q = deque()
    q.append(v)
    graph[v] = 0
    while q:
        v = q.popleft()
        for i in (v + 1, v - 1, v + a, v - a, v + b,  v - b, v * a, v * b):
            if (0 <= i <= 100000) and graph[i] == 0:
                q.append(i)
                graph[i] = graph[v] + 1
                if i == m: # 목표 위치에 도착하면 끝
                    return
                
bfs(n) # n에서부터 탐색
print(graph[m])