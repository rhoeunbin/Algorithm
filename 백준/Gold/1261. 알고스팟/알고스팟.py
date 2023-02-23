from collections import deque

n, m = map(int,input().split())
miro = [list(map(int, input())) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]  # 벽을 깬 횟수를 저장(가중치)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b):
    q = deque() 
    q.append((a, b)) 
    dist[a][b] = 0 

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (nx >= 0) and (nx < m) and (ny >= 0) and (ny < n): # 범위
                if dist[nx][ny] == -1: # 아직 해당 방을 방문하지 않았다면

                    if miro[nx][ny] == 0: # 만약 벽이 없다면
                        dist[nx][ny] = dist[x][y] # 전의 벽을 깬 횟수 그대로 전달
                        q.appendleft((nx, ny))   # 벽이 없는 곳을 우선적으로 돌도록 큐의 맨 왼쪽에 넣어준다
                    else:
                        dist[nx][ny] = dist[x][y] + 1 # 전의 벽을 깬 횟수에서 +1 
                        q.append((nx, ny)) # 큐의 맨 오른쪽에 추가

bfs(0, 0)
print(dist[m - 1][n - 1])