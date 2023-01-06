n = int(input())

cnt = 0 # 0의 개수   
while n > 0:
    cnt += n//5
    n //= 5

print(cnt)