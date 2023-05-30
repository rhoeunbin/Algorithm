n = int(input())
yeol = list(map(int, input().split()))
x = int(input())

start, end = 0, n - 1
cnt = 0
yeol.sort()
while start < end:
    res = yeol[start] + yeol[end]
    if res == x:
        cnt += 1
        start += 1 
        end -= 1
    elif res < x:
        start += 1 # 더 큰 값을 더해야하므로
    else:
        end -= 1 # 더 작은 값을 더해야하므로
print(cnt)