n, m = map(int, input().split())

board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n - 7): # 8*8로 자르기
    for j in range(m - 7):
        ww = 0 # 흰색으로 시작
        bb = 0 # 검은색으로 시작

        for a in range(i, i + 8): # 시작지점
            for b in range(j, j + 8):
                if (a + b) % 2 == 0: # 짝수일 때
                    if board[a][b] != 'B': # B가 아니면
                        ww += 1
                    else:
                        bb += 1
                else:
                    if board[a][b] != 'W':
                        ww += 1
                    else:
                        bb += 1

        result.append(ww)
        result.append(bb)

print(min(result))