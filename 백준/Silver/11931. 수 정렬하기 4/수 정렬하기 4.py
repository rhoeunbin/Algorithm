n = int(input())

num = []
for i in range(n):
    num.append(int(input()))
num.sort(reverse = True)
for i in num:
    print(i)