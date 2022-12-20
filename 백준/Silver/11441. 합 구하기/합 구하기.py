import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))
presum = [num[0]]
for i in range(1, N):
    presum.append(presum[-1] + num[i])


M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(presum[j-1])
    else:
        print(presum[j-1]-presum[i-2])