import sys
input = sys.stdin.readline

n = int(input()) #자릿수

D = [[0 for j in range(2)] for i in range(n+1)]

D[1][1] = 1 # 1은 이친수
D[1][0] = 0 # 이친수는 0으로 시작하지 않기 때문 -> 0으로 끝나는 이친수 X

for i in range(2, n+1):
    D[i][0] = D[i-1][1] + D[i-1][0] # (i번째 0으로 끝나는 개수) = (i-1에서 0으로 끝나는 개수) + (i-1에서 1로 끝나는 개수)
    D[i][1] = D[i-1][0]  # (i번째 1으로 끝나는 개수) = (i-1에서 0으로 끝나는 개수)

print(D[n][0] + D[n][1]) # (n번째에서 0으로 끝나는 개수) + (n번째에서 1로 끝나는 개수)