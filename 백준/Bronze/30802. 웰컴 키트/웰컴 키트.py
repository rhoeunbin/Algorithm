import sys
input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = 0
for i in range(6):
    cnt += size[i] // t
    if size[i] % t != 0:
        cnt += 1

print(cnt)
print(n // p, n % p)