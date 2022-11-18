import sys
input = sys.stdin.readline
n = int(input())
grape = [int(input().rstrip()) for _ in range(n)]
 
#i번째까지 최대로 먹을 수 있는 포도주의 양
d=[0]*n
#i=0인 경우
d[0]=grape[0]
#i=1인 경우
if n>1:
    d[1]=grape[0]+grape[1]
#i=2인 경우
if n>2:
    d[2]=max(d[1],grape[0]+grape[2],grape[1]+grape[2])
#i=n인 경우
for i in range(3, n):
    d[i] = max(grape[i] + grape[i - 1] + d[i - 3], d[i - 2] + grape[i], d[i - 1])
 
print(max(d))