INF = int(1e9)

# 지역, 수색범위, 길의 개수
n, m, r = map(int, input().split())
# 아이템 개수
items = list(map(int, input().split()))
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 최단 경로 담기
ans = 0

# 같은 지점 0처리
for i in range(1, n + 1):
    graph[i][i] = 0

# 그래프 정보
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# 플로이드 워셜
for k in range(1, n + 1): # 거치는 점
    for i in range(1, n + 1): # 시작점
        for j in range(1, n + 1): # 끝점
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # 인덱스 순서 중요

# 시작 지점
for i in range(1, n + 1):
    temp = 0
    # 방문 지점
    for j in range(1, n + 1):
        # 수색 범위 내
        if graph[i][j] <= m:
            # 아이템 회수
            temp += items[j - 1]

    # 이전 시작 지점들과 비교
    ans = max(ans, temp)

print(ans)