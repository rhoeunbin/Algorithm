num = sorted(map(int, input().split()))
res = num[0] + num[1] + min(num[2], num[0] + num[1] - 1)
print(res)