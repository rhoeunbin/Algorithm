import sys
input = sys.stdin.readline

# 빈 칸은 0, 벽은 1
n = int(input())

new = [list(map(int, input().split())) for _ in range(n)] # 새 집의 크기
cnt = 0

# 가로 0 세로 1 대각선 2
def dfs(x, y, d):
    global cnt

    if (x, y) == (n - 1, n - 1):
        cnt += 1
        return

    # 가로 대각선의 경우 가로 이동
    if d == 0 or d == 2:
        if y + 1 < n:
            if new[x][y + 1] == 0:
                dfs(x, y + 1, 0)

    # 세로 대각선의 경우 세로 이동
    if d == 1 or d == 2:
        if x + 1 < n:
            if new[x + 1][y] == 0:
                dfs(x + 1, y, 1)

    # 가로 세로 대각선의 경우 대각선 이동
    if x + 1 < n and y + 1 < n:
        if new[x + 1][y + 1] == 0 and new[x][y + 1] == 0 and new[x + 1][y] == 0:
            dfs(x + 1, y + 1, 2)


dfs(0, 1, 0)
print(cnt)