t = int(input())
paper = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화

for _ in range(t): 
    x, y = map(int, input().split()) 

    for i in range(x, x + 10):  # 세로
        for j in range(y, y + 10):  # 가로
            paper[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿈

result = 0  # 넓이
for k in paper: 
    result += k.count(1) 

print(result) 