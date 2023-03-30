t = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(t):
    con = list(map(str,input().strip()))
    dir= 0
    x_min, y_min, x_max, y_max = 0, 0, 0, 0
    x, y = 0, 0

    for i in con:
        if i == 'F':
            x += dx[dir]
            y += dy[dir]
        elif i == 'B':
            x -= dx[dir]
            y -= dy[dir]
        elif i == 'L':
            if dir == 3: # 동이면
                dir = 0
            else: # 왼
                dir += 1
        elif i == 'R':
            if dir == 0: # 북이면
                dir = 3
            else: # 오
                dir -= 1
        
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x)
        y_max = max(y_max, y)
    # print(x_max, x_min, y_max , y_min)
    print((x_max - x_min) * (y_max - y_min))