import sys
input = sys.stdin.readline

n = int(input())
num = sorted(list(map(int, input().split())))
m = int(input())
card = list(map(int, input().split()))

ans = {}
for i in num:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1


for check in card:
    start, end = 0, n - 1
    exist = 0
    while start <= end:
        mid = (start + end) // 2
        if num[mid] > check:
            end = mid - 1
        elif num[mid] < check:
            start = mid + 1
        else:
            exist = ans[check]
            break
    if exist == 0:
        print(0, end = ' ')
    else:
        print(exist, end = ' ')