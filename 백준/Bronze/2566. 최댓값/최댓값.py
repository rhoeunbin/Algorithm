import sys
input = sys.stdin.readline

board = []
for i in range(9):
    board.append(list(map(int, input().split())))

x, y = 0, 0
max_value = 0

for i in range(9):
    for j in range(9):
        if board[i][j] >= max_value:
            max_value = board[i][j]
            x = i + 1
            y = j + 1

print(max_value)
print(x, y)