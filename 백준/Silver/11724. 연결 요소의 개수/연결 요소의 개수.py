n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)] # 인접 리스트
visited = [False] * (n + 1) # 방문 리스트

def dfs(v):
    visited[v] = True # 방문 리스트에 현재 노드 방문 기록
    for i in arr[v]:
        if not visited[i]: # 방문하지 않은 노드로 dfs 실행
            dfs(i)

for _ in range(m):
    s, e = map(int, input().split()) # 인접 리스트에 그래프 저장
    arr[s].append(e)
    arr[e].append(s)

cnt = 0
for i in range(1, n + 1): # n의 개수만큼 반복
    if not visited[i]: # 방문하지 않은 노드가 있다면
        cnt += 1 # 연결 요소의 개수 +1
        dfs(i)  # dfs 실행

print(cnt)