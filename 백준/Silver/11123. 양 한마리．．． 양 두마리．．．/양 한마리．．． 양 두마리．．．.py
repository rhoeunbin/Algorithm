from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque() # 새로 발견한 양의 위치 저장
    q.append((x, y)) 
    graph[x][y] = '.' # 중복되는 양의 수 방지
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (0 <= nx < h) and (0 <= ny < w) and graph[nx][ny] == '#': # 그래프 안에 탐색하지 않은 양 있으먄
                q.append((nx, ny)) # 새로 발견한 양은 큐에 넣음
                graph[nx][ny] = '.' # 중복되는 양의 수 방지


for _ in range(t):
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]

    ans = 0 # 양 무리 수
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#': # 양이 있는 지점부터
                bfs(i, j)
                ans += 1
    print(ans)