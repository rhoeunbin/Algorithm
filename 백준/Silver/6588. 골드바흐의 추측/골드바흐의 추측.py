import sys
input = sys.stdin.readline

num = [True] * 1000001

for i in range(2, int(len(num)**0.5) + 1):
    if num[i]:
        for j in range(2 * i, 1000001, i):
            num[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n + 1, 2):
        if num[i] and num[n - i]:
            print(n,'=', i,'+',n-i)
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')
