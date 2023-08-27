import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
for _ in range(n):
    cnt += int(input())

print(cnt - (n - 1))