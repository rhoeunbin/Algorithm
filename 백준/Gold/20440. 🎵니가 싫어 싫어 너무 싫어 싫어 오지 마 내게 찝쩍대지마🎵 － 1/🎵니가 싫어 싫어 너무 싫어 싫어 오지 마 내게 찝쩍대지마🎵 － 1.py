import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input()) # 지동이의 방에 출입한 모기의 마릿수
time = defaultdict(int)

for _ in range(n):
    te, tx = map(int, input().split())
    # 모기의 입장 시각 TE과 퇴장 시각 TX
    time[te] += 1
    time[tx] -= 1

mos_max, ber, cur = 0, 0, 0
s, e = 0, 0
flag = 0

for i in sorted(time.keys()):
    bef = cur
    cur += time[i]

    if cur > mos_max:
        mos_max = cur
        s = i
        flag = 1
    elif cur < mos_max and bef == mos_max and flag:
        e = i
        flag = 0

print(mos_max)
print(s, e)