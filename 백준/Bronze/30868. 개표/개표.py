t = int(input())
for i in range(t):
    n = int(input())
    one = n % 5
    plus = n // 5

    print("++++ " * plus + "|" * one)