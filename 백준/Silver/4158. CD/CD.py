while True:
    n, m = map(int,input().split())
    if n== 0 and m == 0:
        break
    dic = {}
    cnt = 0

    for _ in range(n):
        san = int(input())
        dic[san] = 1

    for _ in range(m):
        sun = int(input())
        if sun in dic:
            cnt += 1
    print(cnt)