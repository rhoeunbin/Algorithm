import sys
from collections import deque
input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
answer = []
visited = [-1]*(n+1)

def bfs(start): # 시작 노드
    queue = deque()
    queue.append(start)
    visited[start] += 1
    while queue: # 큐가 비어있을 때까지
        now = queue.popleft()
        for i in arr[now]:
            # 아직 방문 안 한 도시라면
            if visited[i] == -1:
                # 최단 거리 갱신
                visited[i] = visited[now] + 1
                queue.append(i)

# 모든 도로 정보 입력받기
for _ in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)

bfs(x)

for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if not answer: #최단 거리가 K인 도시가 하나도 존재하지 않으면 -1
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
