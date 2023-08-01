from collections import deque

dx = [0, 1, 0, -1] 
dy = [-1, 0, 1, 0]

def dummy():
    dir = 1  # 초기 방향 (우측)
    time = 1  # 시간
    x, y = 0, 0  # 초기 뱀 위치
    snake = deque([(x, y)] ) # 방문 위치
    board[y][x] = 2

    while True:      
        x, y = x + dx[dir], y + dy[dir]
        if (0 <= x < n and 0 <= y < n) and board[y][x] != 2:
            if not board[y][x] == 1:  # 사과가 없는 경우
                b, a = snake.popleft()  # 꼬리 제거
                board[b][a] = 0

            board[y][x] = 2  # 뱀 이동
            snake.append((y, x))

            # if time in turn:  # 뱀의 방향 변환 시간이면 방향 전환
            if time in turn.keys():
                if turn[time] == 'D':  # 오른쪽으로 90도 회전
                    dir = (dir + 1) % 4
                else:  # 왼쪽으로 90도 회전
                    dir = (dir - 1) % 4
            time += 1
        else:
            return time


n = int(input())  # 보드의 크기 N
board = [[0] * n for _ in range(n)]

k = int(input())  # 사과의 개수 K

for _ in range(k):  # 사과의 위치
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

l = int(input())  # 뱀의 방향 변환 횟수 L
turn = {}
# 뱀의 방향 변환 정보
for _ in range(l):
    x, c = input().split()
    turn[int(x)] = c

print(dummy())