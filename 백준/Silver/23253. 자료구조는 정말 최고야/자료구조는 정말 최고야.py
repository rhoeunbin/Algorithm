import sys
input = sys.stdin.readline

n, m = map(int,input().split()) #첫째 줄에 교과서의 수 : n 교과서 더미의 수 : m
order = True # 정렬이 가능한지

for _ in range(m):
    num = int(input())
    book = list(map(int,input().split()))

    for i in range(num-1):
        if book[i] < book[i+1]:
            order = False
            break
    if not order: break

if order:
    print('Yes')
else:
    print('No')