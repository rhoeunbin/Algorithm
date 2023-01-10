import sys
input = sys.stdin.readline

N = int(input())
bi = list(map(int, input().split()))
rebi = list(reversed(bi)) # bi[::-1]

# print(bi, rebi)

increase = [1]*N # 가장 긴 증가 부분 수열 [1 for i in range(N)]
decrease = [1]*N # 가장 긴 감소 부분 수열(reversed)

for i in range(N):
    for j in range(i):
        if bi[i] > bi[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if rebi[i] > rebi[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)


result = [1]*N # [0 for i in range(N)]

for i in range(N):
    result[i] = increase[i] + decrease[N-i-1] -1

print(max(result))