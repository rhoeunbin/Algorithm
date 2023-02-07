n, c = map(int, input().split())
house = []

for _ in range(n):
    x = int(input())
    house.append(x)

house.sort()

# 공유기 사이 거리 최솟값(첫번째 집엔 무조건 공유기를 설치하니까)
start = 1
# 공유기 사이 거리 최댓값//가장 높은 좌표와 가장 낮은 좌표의 차이
end = house[-1] - house[0]

result = 0

while start <= end:
    mid = (start + end) // 2 # 가장 인접한 공유기 사이의 거리
    ordi = house[0] # 공유기 초기 설치 위치
    cnt = 1 # 공유기 설치 개수

    for i in range(1, n):
        if house[i] >= ordi + mid: # gap 이상
            # 공유기 설치 위치 변경
            ordi = house[i]
            # 개수 증가
            cnt += 1
    # c개 이상의 공유기를 설치할 수 있을 때, 공유기 사이 거리 증가
    if cnt >= c:
        start = mid + 1
        result = mid
    # c개 이상의 공유기를 설치할 수 없을 때, 거리 감소
    else:
        end = mid - 1

print(result)