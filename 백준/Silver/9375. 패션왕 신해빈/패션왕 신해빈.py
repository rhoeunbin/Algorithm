import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cloth = {}
    for _ in range(n):
        name, type = input().split()

        if type in cloth.keys():
            cloth[type] += 1
        else:
            cloth[type] = 1            
    # print(cloth)

    ans = 1
    for i in cloth:
        # print(cloth[i])
        ans *= (cloth[i] + 1)
    print(ans - 1)