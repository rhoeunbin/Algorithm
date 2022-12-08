for _ in range(4):
    x, y, p, q, x1, y1, p1, q1 = map(int, input().split())

    if p < x1 or p1 < x or y > q1 or q < y1:# 공통부분이 없음
        print('d')
        continue
    elif x == p1 or p == x1:
        if q == y1 or y == q1: # 점
            print('c')
            continue
        else: # 선분
            print('b')
            continue
    elif q == y1 or q1 == y:
            print('b')
            continue
    else: # 직사각형
        print('a')
        continue