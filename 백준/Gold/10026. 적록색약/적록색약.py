import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
matrix = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

common, yesol = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    #현재 색상 좌표 방문
    visited[x][y] = True
    current = matrix[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            #현재 좌표 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로
            if visited[nx][ny] == False:
                if matrix[nx][ny] == current:
                    dfs(nx, ny)

# 적록색약 아닐 때
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로
        if visited[i][j] == False:
            dfs(i, j)
            common += 1

# 적록색약일 때 R을 G로 바꿈 
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            yesol += 1

print(common, yesol)
