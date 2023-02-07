n, m = map(int,input().split()) # N : 레슨 수 , M : 블루레이 수
a = list(map(int, input().split())) # 기타 레슨 데이터 저장 리스트
start = 0
end = 0

for i in a:
    if start < i:
        start = i # 시작 인덱스 저장(num 리스트 중 최댓값)
    end += i # 종료 인덱스 저장(num 리스트의 총합)

while start <= end:
    mid = int((start + end) / 2)
    lesson_sum = 0 # 레슨 합
    cnt = 0 # 현재 사용한 블루레이 개수

    for i in range(n):
        if lesson_sum + a[i] > mid:
            cnt += 1
            lesson_sum = 0 # 현재 블루레이에 저장할 수 없어 새로운 블루레이로 교체
        lesson_sum += a[i]

    if lesson_sum != 0:  # sum이 0이 아니면 마지막 블루레이가 필요함 => cnt 올리기
        cnt += 1
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)