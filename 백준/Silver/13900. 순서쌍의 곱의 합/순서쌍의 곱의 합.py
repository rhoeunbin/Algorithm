n = int(input())
num = list(map(int, input().split()))

cnt = 0
sum_num = sum(num) # 9
for i in num:
    sum_num -= i
    cnt += sum_num * i # 7 * 2 + 4 * 3 + 0* 4 = 26

print(cnt)