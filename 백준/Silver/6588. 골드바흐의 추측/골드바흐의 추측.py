import sys
input = sys.stdin.readline

def gold(a):
    if a == 1:
        return False
    else:
        for i in range(2, int(a**0.5)+1):
            if a % i == 0: 
                return False
        return True

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n+1, 2):
        if gold(i):
            if gold(n-i):
                print(n,'=', i,'+',n-i)
                break
