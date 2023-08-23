import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    v.reverse()
    # print(v)
    max_v = v[0]
    res = 0

    for i in range(1, n):
        if max_v < v[i]:
            max_v = v[i]
            continue
        res += max_v - v[i]
    print(res)