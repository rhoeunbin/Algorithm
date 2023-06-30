from collections import deque

def dfs(x, y , num):
    if len(num) == 6:
        if num not in res: # 똑같은 숫자가 있는지 확인
            res.append(num)
        return

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + graph[nx][ny])


graph = [list(map(str, input().split())) for _ in range(5)]
res = []
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
print(len(res))