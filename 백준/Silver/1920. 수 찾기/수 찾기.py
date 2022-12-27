import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
num.sort()
m = int(input())
target_list = list(map(int,input().split()))

for i in range(m):
    find = False # 찾아야 하는 수
    target = target_list[i]
    # 이진 탐색 시작
    start = 0 # 시작 인덱스
    end = len(num)-1 # 종료 인덱스

    while start <= end:
        midi = int((start+end) / 2) # 중간 인덱스
        midv = num[midi]# 중앙값

        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    
    if find:
        print(1)
    else:
        print(0)