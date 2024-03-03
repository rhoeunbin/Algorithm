import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))
ans = {}

for i in card:
    ans[i] = 0

for j in num:
    if j in ans:
        ans[j] = 1

for k in ans:
    print(ans[k], end = ' ')