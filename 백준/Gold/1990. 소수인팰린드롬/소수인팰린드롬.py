import sys
input = sys.stdin.readline

a, b = map(int,input().split())

#10,000,000 이상인 팰린드롬수는 존재 X
if b > 10000000:
    b = 10000000

def Prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

palindrome = [n for n in range(a, b+1) if str(n) == str(n)[::-1]]        
for n in palindrome:
    if Prime(n):
        print(n)
print(-1)