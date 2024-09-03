t = int(input())

for _ in range(t):
    n = int(input())
    memo_one = set(map(int, input().split()))
    m = int(input())
    memo_two = list(map(int, input().split()))

    for i in memo_two:
        if i in memo_one:
            print(1)
        else:
            print(0)