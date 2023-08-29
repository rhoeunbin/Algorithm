s = input()

while s:
    if s == s[::-1]:
        print(1)
        break
    else:
        print(0)
        break