import sys
input = sys.stdin.readline

n = int(input()) # 재료의 개수
m = int(input()) # 갑옷을 만드는데 필요한 수
num = list(map(int, input().split())) # N개의 재료들이 가진 고유한 번호
num.sort()

ans = 0
start = 0
end = n - 1

while start < end:
    if num[start] + num[end] < m:
        start += 1
    elif num[start] + num[end] > m:
        end -= 1
    else:
        ans += 1
        start += 1
        end -= 1

print(ans)