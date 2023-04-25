n = int(input())
cnt = 1
start, end = 1, 1
hop = 1 # n = 15일 때 숫자 15만 뽑는 경우의 수를 미리 넣고 초기화 하기 때문

# 투 포인터 이동 원칙
while end != n: # end가 n이 될 때까지 반복
    if hop == n:
        cnt += 1
        end += 1
        hop += end
    elif hop > n:
        hop -= start
        start += 1
    else:
        end += 1
        hop += end

print(cnt)