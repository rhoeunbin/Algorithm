num = [list(map(int, input().split())) for _ in range(int(input()))]

for i in range(len(num)):
    a = num[i][0] % 10
    b = num[i][1]
    # print('num',a, b)
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print((a**2) % 10)
        else:
            print(a % 10)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        print((a ** b) % 10)    