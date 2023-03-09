import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [0 for _ in range(101)]

for _ in range(n + m):
    x, y =  map(int, input().split()) # 사다리의 정보// x번 칸에 도착하면, y번 칸으로 이동한다
    graph[x] = y

visited = [0 for _ in range(101)]
directions = list(range(1, 7))
cnt = 0

def bfs(start, cnt): # (시작점, 횟수)
    q = deque()
    q.append((start, cnt))
    visited[start] = True
    while q:
        now, t = q.popleft()
        if now == 100: # 100번 칸에 도착하면
            print(t) # 굴린 횟수 출력
            break # 반복문 탈출
        for i in range(6):
            next = now + directions[i] # 다음 이동 위치
            if 1 <= next <= 100 and not visited[next]:
                visited[next] = True
                if graph[next] == 0:  # 사다리나 뱀이 있으면 그 칸은 지나치고 무조건 사다리나 뱀을 타야함
                    q.append((next, t + 1))
                else:
                    q.append((graph[next], t + 1))
bfs(1, 0)