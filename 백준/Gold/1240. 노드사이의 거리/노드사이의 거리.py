import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, end):
    queue = deque() 
    queue.append((start,0)) #현재 노드 방문 처리
    visited = [False] * (N + 1) #노드가 방문된 정보
    visited[start] = True 
    while queue:
        node, dis = queue.popleft() # 큐에서 값 뽑아서
        
        if node == end: #찾고 있는 노드와 번호가 일치하면
            return dis # 인접 탐색
        
        for i, len in graph[node]: #
            if not visited[i]:
                visited[i] = True
                queue.append((i, dis + len)) # queue에 가까운 노드, 거리 기록 추가
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, len = map(int,input().split())
    graph[a].append((b, len))
    graph[b].append((a, len))

for _ in range(M):
    a, b = map(int,input().split())
    print(bfs(a, b))