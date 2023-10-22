m = int(input())
d = int(input())

if m == 1 and d <= 31:
    print("Before")
if m == 2:
    if d < 18:
        print("Before")
    elif d == 18:
        print("Special")
    else:
        print("After")

if m >= 3:
    print("After")