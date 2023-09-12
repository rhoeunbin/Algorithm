import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F + 1)]


def bfs():
    q = deque()
    q.append(S)
    visited[S] = True

    while q:
        y = q.popleft()
        if y == G:
            return visited[y] - 1

        for i in (y + U, y - D):
            if (0 < i <= F) and not visited[i]:
                visited[i] = visited[y] + 1
                q.append(i)
            
    return "use the stairs"
print(bfs())