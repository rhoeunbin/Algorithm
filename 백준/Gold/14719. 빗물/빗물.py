h, w = map(int,input().split())
block = list(map(int,input().split()))

rain = 0
for i in range(1, w - 1): # 양 옆에는 고일 수 없음
    left = max(block[:i]) # 왼쪽에서 제일 높은 블럭
    right = max(block[i + 1:]) # 오른쪽에서 제일 높은 블럭

    low = min(left, right) # 둘 중 낮은 블럭

    if block[i] < low: # 현재 블럭 < 둘 중 낮은 블럭
        rain += low - block[i] # 빗물 양 += 둘 중 낮은 블럭 - 현재 블럭
print(rain)