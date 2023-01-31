n = int(input())
direc = list(map(int, input().split()))

ans = [0] * n
cnt = 0
for i in range(n):
    if direc[i] == 1:
        cnt += 1
    else:
        cnt -= 1
    ans.append(cnt)
print(max(ans) - min(ans))    
