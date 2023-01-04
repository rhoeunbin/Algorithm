import sys
input = sys.stdin.readline

#표의 크기 N과 합을 구해야 하는 횟수 M
N, M = map(int,input().split())
arr = [[0] * (N + 1)] # 원본 리스트
D = [[0] * (N + 1) for _ in range(N + 1)] # 합 배열

for _ in range(N):
    arr_row = [0] + [int(x) for x in input().split()]
    arr.append(arr_row)

for i in range(1, N+1):
    for j in range(1, N+1):
        # 합 배열
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    # 구간 합 배열로 질의에 답변
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)