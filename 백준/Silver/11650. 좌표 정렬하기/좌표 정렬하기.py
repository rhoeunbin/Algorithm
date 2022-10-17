import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    [x, y]= map(int,input().split())
    array.append([x,y])

s_array = sorted(array)

for i in range(n):
    print(s_array[i][0], s_array[i][1])