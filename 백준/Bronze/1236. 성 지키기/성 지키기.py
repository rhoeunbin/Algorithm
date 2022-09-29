n, m = map(int,input().split())
matrix = []

for _ in range(n): #이차원 리스트 만들기
    line = list(input())
    matrix.append(line)

cnt1 = 0
cnt2 = 0
for i in range(n): #행의 개수만큼
    if 'X' not in matrix[i]: #만약 행에 X가 없다면 
        cnt1 += 1

for j in range(m): #열의 개수만큼
    if "X" not in [matrix[i][j] for i in range(n)] :  #만약 열에 X가 없다면
        cnt2 += 1
print(max(cnt1, cnt2))