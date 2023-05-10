import sys
input = sys.stdin.readline
import heapq

# N (1 <= N <= 50,000) 개의 헛간과, 소들의 길인 M (1 <= M <= 50,000) 개의 양방향 길이
n, m = map(int,input().split())
INF = sys.maxsize
graph = [[] for _ in range(n + 1)]
dis = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0

    while q:
        cost, node = heapq.heappop(q) # 거리, 현재 노드
        if dis[node] < cost: # 현재 노드에 연결된 엣지 탐색
            continue
        for n, c in graph[node]:
            if cost + c < dis[n]:
                dis[n] = cost + c
                heapq.heappush(q, (cost + c, n))
dijkstra(1)
print(dis[n])