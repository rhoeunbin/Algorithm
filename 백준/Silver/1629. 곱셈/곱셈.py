import sys
input = sys.stdin.readline

# A, B, C = map(int,input().split())

# print((A**B)%C) => 시간초과

# 분할 정복으로 풀기
def multi(a,b,c):
    if b == 1:
        return a % c
    # 짝수면
    if b % 2 == 0:
        return (multi(a,b//2,c) ** 2)%c
    else:
        return ((multi(a,b//2,c) ** 2)*a)%c

a,b,c = map(int,input().split())
print(multi(a,b,c))