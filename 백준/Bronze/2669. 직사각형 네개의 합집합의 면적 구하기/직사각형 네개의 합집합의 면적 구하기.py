import sys
input = sys.stdin.readline

#어제 2차원 배열의 합이랑 같은 문제인 것 같음
rec = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            rec[x][y] = 1 #사각형의 넓이는 1

sum_ = 0            
for row in rec :
    sum_ += sum(row)
print(sum_)
