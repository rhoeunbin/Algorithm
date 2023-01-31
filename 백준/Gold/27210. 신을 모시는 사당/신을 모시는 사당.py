n = int(input())
direc = list(map(int, input().split()))

cnt_l, cnt_r = [0] * n, [0] * n  # 왼쪽 1 리스트, 오른쪽 2 리스트

for i in range(n):
    if direc[i] == 1:  
        cnt_l[i] = cnt_l[i - 1] + 1  
        cnt_r[i] = max(0, cnt_r[i - 1] - 1)
    else:  
        cnt_r[i] = cnt_r[i - 1] + 1 
        cnt_l[i] = max(0, cnt_l[i - 1] - 1)

print(max(max(cnt_l), max(cnt_r)))  # 둘 중 최대값