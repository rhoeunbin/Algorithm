import sys
input = sys.stdin.readline

# 수의 개수 N과 합을 구해야 하는 횟수 M
N, M = map(int, input().split())
n_num = list(map(int, input().split()))
prefix = [0]
ans = 0

for x in n_num:
    ans = ans + x
    # print(ans)
    prefix.append(ans)
# print(prefix)

for n in range(M):
    i, j = map(int,input().split())
    print(prefix[j] - prefix[i-1])

# print(n_num)