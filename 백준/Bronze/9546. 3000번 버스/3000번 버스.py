for t in range(int(input())):
    k = int(input()) # 정류장의 수
    p = 1
    for i in range(k - 1):
        p = p * 2 + 1
    print(p)