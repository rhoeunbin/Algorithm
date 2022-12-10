import sys
input = sys.stdin.readline

N, M, B = map(int,input().split())
block = [list(map(int, input().split())) for _ in range(N)]
ans = int(1e9) # 1e9 = 1*109 = 1000000000
glevel = 0 # 땅의 높이

for i in range(257): #땅 높이 => 0층부터 256층까지 반복
    use_block, take_block = 0, 0 # 가져온 블록(take_block), 사용한 블럭(use_block)

    # 반복문을 통해 블록을 확인
    for x in range(N):
        for y in range(M):

            # 블록이 층수보다 더 크면
            if block[x][y] > i:
                take_block += block[x][y] - i
            # 블록이 층수보다 더 작으면
            else:
                use_block += i - block[x][y]
    # 블록을 뺀 것과 원래 있던 블록의 합과 블록을 더한 값을 비교
    # 블록을 뺀 것과 원래 있던 블록의 합이 더 커야 층을 만들 수 있음.
    if use_block > take_block + B:
        continue

    count = take_block * 2 + use_block

    if count <= ans:
        # 0부터 256층까지 비교하므로 업데이트 될수록 고층의 최저시간
        ans = count # 최저 시간
        glevel = i

print(ans, glevel)
