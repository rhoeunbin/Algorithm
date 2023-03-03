import sys
from collections import deque

def bfs(v):
    q = deque([v])

    while q:
        v = q.popleft()
        if v == k: # 동생의 위치랑 같으면 종료
            return visited[v]
        for i in (v-1, v+1, 2*v): # 이동할 수 있는 방향
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

n, k = map(int,input().split())
visited = [0 for i in range(100001)]
print(bfs(n))