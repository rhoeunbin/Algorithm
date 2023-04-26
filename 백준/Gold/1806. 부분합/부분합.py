import sys

n, s = map(int, input().split())
num = list(map(int, input().split()))

start, end = 0, 0
total = 0
ans = n + 1

while True:
    if total >= s:
        ans = min(ans, end - start)
        total -= num[start]
        start += 1
    elif end == n:
        break
    else:
        total += num[end]
        end += 1

if ans == n + 1:
    print(0)

else:
    print(ans)