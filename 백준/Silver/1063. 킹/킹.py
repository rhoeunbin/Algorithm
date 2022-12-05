import sys
input = sys.stdin.readline

# 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.
# ord => 문자 -> 정수 // chr -> 정수-> 문자

p = [0, 1, 2, 3, 4, 5, 6, 7, 8]
cs = {'R':[0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0], 'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}
king, stone, n = input().rstrip().split()

kx, ky = 8 - int(king[1]), p[ord(king[0]) - 65]
sx, sy = 8 - int(stone[1]), p[ord(stone[0]) - 65]

maps = [[0] * 8 for _ in range(8)]

for _ in range(int(n)):
    command = input().rstrip()
    dx, dy = cs[command]

    nx = kx + dx
    ny = ky + dy
    if 0 <= nx < 8 and 0 <= ny < 8 and 0 <= sx < 8 and 0 <= sy < 8:
        if nx == sx and ny == sy:
            if 0 <= sx + dx < 8 and 0 <= sy + dy < 8:
                sx, sy = sx + dx, sy + dy
                kx, ky = nx, ny
            else:
                continue
        else:
            kx, ky = nx, ny

r1, r2 = "", ""
r1 += chr(p[ky] + 65)
r1 += str(8 - kx)

r2 += chr(p[sy] + 65)
r2 += str(8 - sx)

print(r1)
print(r2)