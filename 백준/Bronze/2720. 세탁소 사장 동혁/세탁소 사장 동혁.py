t = int(input())
c = [25, 10, 5, 1]
for i in range(t):
    money = int(input())
    for i in c:
        print(money // i, end=' ')
        money = money % i