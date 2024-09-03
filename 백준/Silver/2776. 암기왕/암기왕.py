t = int(input())

for _ in range(t):
    n = int(input())
    memo_one = list(map(int, input().split()))
    memo_one.sort()
    m = int(input())
    memo_two = list(map(int, input().split()))

    for i in range(m):
        find = False
        t = memo_two[i] # 찾아야 하는 수
        start = 0
        end = n - 1
        while start <= end:
            midi = int((start + end) / 2) # 중간 인덱스
            midv = memo_one[midi] # 중앙값
            if midv > t: # 중앙값 > 타겟
                end = midi - 1 # 끝에서 -1
            elif midv < t:
                start = midi + 1 # 앞에서 +1
            else:
                find = True # 찾음 => 1
                break
        if find:
            print(1)
        else:
            print(0)