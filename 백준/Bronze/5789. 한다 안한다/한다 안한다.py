n = int(input())
for i in range(n):
    s = list(input())
    temp = len(s) // 2 - 1
    if s[temp] == s[-temp - 1]:
        print("Do-it")
    else:
        print("Do-it-Not")