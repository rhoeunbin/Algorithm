import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
hop = [0]

cnt = 0

for i in num:
    cnt += i
    hop.append(cnt)

for i in range(m):
    s, e = map(int, input().split())
    print(hop[e] - hop[s - 1])