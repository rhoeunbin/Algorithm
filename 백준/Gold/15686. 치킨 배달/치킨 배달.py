from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 폐업시키지 않을 치킨집을 최대 M개
city = [list(map(int, input().split())) for _ in range(N)]
# 0은 빈 칸, 1은 집, 2는 치킨집
answer = int(1e9)
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))


for combi in combinations(chicken, M):
    total = 0 # 도시 치킨 거리
    for h in house:
        distance = int(1e9) # 각 집마다의 치킨 거리
        for c in combi:
            distance = min(distance, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        total += distance
    answer = min(answer, total)

print(answer)