dic = {}

for _ in range(7):
    semina, num = input().split()
    dic[semina] = int(num)
print(max(dic, key=dic.get))