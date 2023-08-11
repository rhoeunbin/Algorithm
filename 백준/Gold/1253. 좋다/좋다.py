n = int(input())
num = list(map(int, input().split()))

num.sort()
cnt = 0

for i in range(n):
    find = num[i]
    start = 0
    end = n - 1

    while start < end: # end가 더 클 때까지
        if num[start] + num[end] == find:
            # 두 포인터 start, end가 i가 아닐 때 좋은 수 개수 +1
            if start != i and end != i:
                cnt += 1 
                break
            # 두 포인터 start, end가 i가 맞을 때 포인터 변경 및 계속 수행
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif num[start] + num[end] < find:
            start += 1 # 포인터 start 증가
        else:
            end -= 1 # 포인터 end 감소
print(cnt)