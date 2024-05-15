n = int(input())
num = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in range(n):
    if v == num[i]:
        cnt += 1
print(cnt)