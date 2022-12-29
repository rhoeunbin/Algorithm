import sys
input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0,i+1):
        if j == 0: # tri[0][0], tri[1][0], tri[2][0],,
            tri[i][j] = tri[i][j] + tri[i - 1][j]
        elif i == j:  # tri[1][1], tri[2][2], tri[3][3],,
            tri[i][j] = tri[i][j] + tri[i - 1][j - 1]
        else: # tri[2][1], tri[3][1], tri[3][2]
            tri[i][j] = max(tri[i - 1][j - 1], tri[i - 1][j]) + tri[i][j]

print(max(tri[n - 1]))
