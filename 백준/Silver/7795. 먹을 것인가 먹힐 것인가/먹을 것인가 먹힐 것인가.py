import sys
input = sys.stdin.readline

def binary_search(target,data):
    start = 0
    end = len(data) - 1
    res = -1
    while start <= end :
        mid = (start + end) // 2
        if data[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    # print(a, b)

    ans = 0
    for i in a:
        ans += binary_search(i, b) + 1

    print(ans)