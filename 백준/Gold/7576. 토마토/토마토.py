from collections import deque

m, n = map(int,input().split())
graph = []
q = deque(())

for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
# print(graph)

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표 크기를 넘어가면 X, 그 좌표에 토마토가 익지 않은 상태(0)
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 익히고 1을 더해주면서 횟수를 세기
                # 여기서 나온 제일 큰 값이 정답
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))
bfs()
ans = 0
for i in graph:
    for j in i:
        if j == 0:
            # 다 찾아봤는데 토마토가 안 익음
            print(-1)
            exit(0)
    # 다 익혔으면 최댓값 => 정답
    ans = max(ans, max(i))
print(ans - 1) # 처음 시작이 1 => 1을 뺌