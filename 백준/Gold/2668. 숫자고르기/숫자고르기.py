n = int(input())
dic = {}
for i in range(n):
    dic[i+1] = int(input())
# 1 2 3 4 5 6 7 key
# 3 1 1 5 5 4 6 value
while True:
    baseSet = set(dic.values()) # 1 3 4 5 6
    dic = {key:value for key, value in dic.items() if key in baseSet}
    if baseSet == set(dic.values()):
        break
print(len(dic))
for key in dic.keys():
    print(key)