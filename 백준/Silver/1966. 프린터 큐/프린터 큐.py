from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    q = deque(list(map(int,input().split())))
    idx = deque(list(range(n)))
    ans = 0

    while q:
        if q[0] == max(q):
            ans += 1
            q.popleft()
            d_idx = idx.popleft()

            if d_idx == m:
                print(ans)

        else:
            q.append(q.popleft())
            idx.append(idx.popleft())