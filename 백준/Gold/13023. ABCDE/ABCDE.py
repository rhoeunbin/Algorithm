import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for i in range(n)] # 친구 관계그래프
visited = [0] * n
result = 0 # 정답 변수

for i in range(m):
    a, b = map(int,input().split()) 
    graph[a].append(b)
    graph[b].append(a)

def dfs(depth, x):# 깊이,현재 노드
    global result
    if depth == 4: # 친구 관계가 4번 이상 연결
        result = True # 정답 표시 후 return
        return
    visited[x] = True # 방문 표시

    for i in graph[x]: # 친구 관계 있는지 파악
        if not visited[i]: # 방문 안 했으면

            dfs(depth + 1, i) # 재귀 수행 => 깊이 계속 수행
    visited[x] = False # 방문 표시 해제


for i in range(n):
    dfs(0, i)
    if result: # 친구 관계가 있으면
        break # 탈출

if result: # 정답 있으면 1
    print(1)
else: # 정답 없으면
    print(0)