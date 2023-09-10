l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c == 0 :
  ac = a // c
else :
  ac = (a // c) + 1

if b % d == 0 :
  bd = b // d
else :
  bd = (b // d) + 1

print(l - max(ac, bd))