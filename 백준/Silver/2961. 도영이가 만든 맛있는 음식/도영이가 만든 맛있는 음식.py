import sys, itertools
from itertools import combinations
input = sys.stdin.readline

n = int(input())
sour = []
bitter = []
for _ in range(n):
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)

answer = 1000000000

for i in range(1, n+1): # 재료를 i개 뽑을 때
    combi = list(combinations(list(range(n)), i)) # 가능한 경우를 담은 리스트

    for c in combi: # 경우 하나씩 탐색
        ss = 1 # 신맛 => 1부터 곱
        bb = 0 # 쓴맛 => 0부터 더함

        for j in range(i): # 맛 계산
            ss *= sour[c[j]]
            bb += bitter[c[j]]
        answer = min(answer, abs(ss-bb))

print(answer)