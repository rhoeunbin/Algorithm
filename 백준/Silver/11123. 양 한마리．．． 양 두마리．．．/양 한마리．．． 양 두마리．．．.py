from collections import deque

t = int(input())
d = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 이동 좌표값

def bfs(x, y):
    q = deque() # 새로 발견한 양의 위치 저장
    q.append((x, y)) 
    graph[x][y] = '.' # 중복되는 양의 수 방지
    while q:
        x, y = q.popleft()
        for dy, dx in d: # 인접 양 찾기
            nx, ny =  x + dx, y + dy
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