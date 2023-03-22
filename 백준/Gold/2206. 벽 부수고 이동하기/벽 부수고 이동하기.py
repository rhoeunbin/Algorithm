from collections import deque
n, m = map(int, input().split())

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
graph = [list(map(int, input())) for _ in range(n)]

def bfs():
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]    

    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()

        # 목표지점 도달 시 해당 위치까지의 거리 리턴
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if not visited[nx][ny][w] and graph[nx][ny] == 0: # 방문하지 않고 육지라면
                    visited[nx][ny][w] = visited[x][y][w] + 1 # 다음 좌표로 넘어갈 때 +1
                    q.append((nx, ny, w)) 

                # 현재 위치가 벽이고, 벽을 아직 부수지 않았다면
                elif graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    q.append((nx, ny, w + 1))
    return -1

print(bfs())