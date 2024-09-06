l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c == 0 :
    cnt1 = a // c
else :
    cnt1 = (a // c) + 1

if b % d == 0 :
    cnt2 = b // d
else :
    cnt2 = (b // d) + 1

print(l - max(cnt1, cnt2))