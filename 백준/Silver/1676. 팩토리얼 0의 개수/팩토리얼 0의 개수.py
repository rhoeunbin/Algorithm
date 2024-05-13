n = int(input())
cnt = 0

while (n > 1):
    cnt += n // 5 # 25 와 125같은 제곱수를 생각
    n = n // 5
print(cnt)