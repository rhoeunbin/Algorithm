from collections import deque

n, m, start = map(int,input().split())
# 노드 개수, 엣지 개수, 시작점
arr = [[] for _ in range(n + 1)] # 인접 리스트에 그래프 데이터 저장

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n + 1):
    arr[i].sort()
# 방문할 수 있는 노드가 여러 개일 경우, 번호가 작은 것을 먼저 방문하기 위해 정렬

def dfs(v):
    print(v, end=' ') # 현재 노드 출력
    visited[v] = True # visiter 리스트에 현재 노드 방문 기록
    for i in arr[v]: # 현재 노드의 연결 노드 중 방문하지 않은 노드로 dfs 실행(재귀함수형태)
        if not visited[i]:
            dfs(i)

visited =[False] * (n + 1) # visited 리스트 초기화
dfs(start) # dfs 실행

def bfs(v):
    q = deque()
    q.append(v) # 큐 자료구조에서 시작 노드 삽입
    visited[v] = True
    while q: # 큐가 비어있을 때까지
      now_node = q.popleft()
      print(now_node, end = ' ') # 가져온 노드 출력

      # 현재 노드의 연결 노드 중 미 방문 노드를 큐에 삽입하고 방문 리스트에 기록
      for i in arr[now_node]:
          if not visited[i]:
              visited[i] = True
              q.append(i)

print()
visited = [False] * (n + 1)
bfs(start)