import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

start = 0
cnt = 0
ans = 0

for end in range(len(arr)):
    cnt += 1
    # print(arr[end], arr[start])

    while arr[end] - arr[start] > 4:
        start += 1
        cnt -= 1
    # print(cnt)
    ans = max(ans, cnt)
print(5 - ans)