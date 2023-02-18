n, m, l = map(int,input().split())
# 현재 휴게소의 개수 N, 더 지으려고 하는 휴게소의 개수 M, 고속도로의 길이 L

rest = [0] + list(map(int,input().split())) + [l]
rest.sort()

start, end = 1, l - 1
ans = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, len(rest)):
      # 현재 인덱스 - 이전 인덱스가 mid 보다 커야 휴게소 설치 가능
        if rest[i] - rest[i - 1] > mid:
          # 나눈 만큼 휴게소 설치(현재 설치 구역은 제외이므로 - 1)
            cnt += (rest[i] - rest[i - 1] - 1) // mid
    if cnt > m: # m보다 더 지었다면
        start = mid + 1 # 설치하는 간격 넓혀야하니깐 +1

    else:
        end = mid -1
        ans = mid
print(ans)
