import sys
from collections import deque

def check_right(start, d):
    if start > 4 or gears[start - 1][2] == gears[start][6]: # 더 이상 조사 X
        return
    # 오른쪽 확인
    if gears[start - 1][2] != gears[start][6]:
        check_right(start + 1, -d) # 인접한 톱니바퀴가 회전 가능한지 파악
        gears[start].rotate(d)

def check_left(start, d):
    if start < 1 or gears[start][2] == gears[start + 1][6]:
        return
    # 왼쪽 확인
    if gears[start + 1][6] != gears[start][2]:
        check_left(start - 1, -d)
        gears[start].rotate(d)

gears = {}
for i in range(1, 5):
    gears[i] = deque(list(map(int, input().replace('\n',''))))

k = int(input())
for i in range(k): 
    n, d = map(int, input().split()) # n : 회전시킨 톱니바퀴 번호, d : 방향
    # 1이면 시계, -1이면 반시계
    # 기준 톱니바퀴가 주어지면 오른쪽, 왼쪽 회전이 가능한지 확인하고 회전
    check_right(n + 1, -d)
    check_left(n - 1, -d)
    gears[n].rotate(d) # 기준 톱니바퀴 회전

result = 0
for i in range(4):
    result += (2 ** i) * gears[i + 1][0]
print(result)