t = int(input())
for _ in range(t):
    n = input().lower()
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")