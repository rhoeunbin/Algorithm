num = map(int, input().split())

res = 0

for i in num:
    res += i ** 2

print(res % 10)  
        