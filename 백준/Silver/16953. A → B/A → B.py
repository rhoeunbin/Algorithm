import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    q = deque([(a, 1)])

    while q:
        x, y = q.popleft()
        if x == b:
            print(y)
            return

        if x * 2 <= b:
            q.append((x * 2, y + 1))
        if x * 10 + 1 <= b:
            q.append((x * 10 + 1, y + 1))
    print(-1)


a, b = map(int, input().split())
bfs(a, b)