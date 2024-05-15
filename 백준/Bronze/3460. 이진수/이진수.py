for _ in range(int(input())):
    n = int(input())
    ans = 0
    while n > 0:
        if n % 2 == 1:
            print(ans, end=" ")
        n = n // 2
        ans += 1
