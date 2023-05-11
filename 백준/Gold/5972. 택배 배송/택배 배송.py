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
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0

    while q:
        cost, node = heapq.heappop(q) # heapq에서 데이터 가져옴 (거리, 현재 노드)
        if dis[node] < cost: # 현재 노드까지의 비용이 cost보다 작으면 continue
            continue
        for n, c in graph[node]: # 현재 노드에 연결된 엣지 탐색하면서 최소 거리 구함
            if cost + c < dis[n]: # 새로운 총 거리가 새로운 노드의 n번째 최단거리보다 작다면
                dis[n] = cost + c # 새로운 노드의 n번째 최단 거리를 새로운 총 거리로 변경하고
                heapq.heappush(q, (cost + c, n)) # 큐에 새로운 데이터 추가(거리, 노드)
dijkstra(1) # 현서 위치가 1
print(dis[n]) # 찬홍이 위치가 n