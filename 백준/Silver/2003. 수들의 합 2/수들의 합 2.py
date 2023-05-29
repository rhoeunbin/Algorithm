n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
start, end = 0, 1

while (start <= end and end <= n):
    total = sum(a[start : end])

    # 구간의 합 < 목푯값
    if total < m:
        end += 1 # 끝 인덱스 오른쪽 한 칸 이동

    # 구간의 합 > 목푯값
    elif total > m:
        start += 1
    
    # 구간의 합 = 목푯값
    else:
        cnt += 1
        end += 1

print(cnt)