x = int(input())

length = [64, 32, 16, 8, 4, 2, 1 ]
cnt = 0
for i in range(len(length)):
    if x >= length[i]:
        x -= length[i]
        cnt += 1
    
    if x == 0:
        break
print(cnt)