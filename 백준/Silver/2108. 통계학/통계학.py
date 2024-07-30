n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

num.sort()
print(round(sum(num)/n))
print(num[n//2])

dic = {}
for a in num:
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1
max_cnt = max(dic.values())
max_arr = []

for i in dic:
    if max_cnt == dic[i]:
        max_arr.append(i)

if len(max_arr)>1:
    print(max_arr[1])
else:
    print(max_arr[0])

print(num[-1] - num[0])