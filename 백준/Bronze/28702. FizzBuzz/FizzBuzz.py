import sys
input = sys.stdin.readline

i = 0
for t in [3, 2, 1]:
    s = input().rstrip()

    if s not in ["FizzBuzz", "Fizz", "Buzz"]:
        i = int(s) + t

if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
elif i % 3 == 0 and not i % 5 == 0:
    print("Fizz")
elif i % 5 == 0 and not i % 3 == 0:
    print("Buzz")
else:
    print(i)
