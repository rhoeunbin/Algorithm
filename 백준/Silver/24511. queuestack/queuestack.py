import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

ans = deque()
for i in range(n):
    if a[i] == 0:
        ans.appendleft(b[i])

for j in range(m):
    ans.append(c[j])
    print(ans.popleft(), end = ' ')