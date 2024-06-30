k, n = map(int, input().split())
lan = []

for _ in range(k):
    lan.append(int(input()))

start, end = 1, max(lan) # 1부터 가장 긴 길이까지 

while (start <= end): # 잘린 랜선 개수가 n보다 많으면 mid 밑으로 볼 필요 X
    mid = (start + end) // 2
    cnt = 0

    for i in range(k):
        cnt += lan[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)