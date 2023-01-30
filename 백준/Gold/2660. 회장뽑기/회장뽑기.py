from pprint import pprint

INF = int(1e9)
n = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    graph[i][i] = 0

# 그래프 정보
while True:
    a, b = map(int, input().split())
    # 입력 시 -1, -1일 때
    if a == -1 and b == -1:
        break
    # 그래프 초기화
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

score = []

for s in range(1, n +1):
    score.append(max(graph[s][1:]))

candiate = score.count(min(score))
print(min(score), candiate)

for k, v in enumerate(score):
    if v == min(score):
        print(k + 1, end=' ')