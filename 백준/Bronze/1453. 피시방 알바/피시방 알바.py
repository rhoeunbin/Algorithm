n = int(input())
list_ = []
num = input().split()
cnt = 0  #거절당하는 사람 수

for i in range(n):
    
    if num[i] not in list_:
        list_.append(num[i])
    else :
        cnt += 1

print(cnt)