import sys
input = sys.stdin.readline
import pprint

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n): # graph[i][j] 보다 graph[i][k] + graph[k][j]가 작으면 업데이트
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# A(1 ≤ A ≤ N) 는 서비스를 요청한 손님이 위치한 파티장의 번호
# B(1 ≤ B ≤ N) 다음 파티가 열리는 파티장의 번호
# C(1 ≤ C ≤ 1,000,000,000)는 지금으로부터 다음 파티가 열리는데 걸리는 시간
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")