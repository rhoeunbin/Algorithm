import sys
input = sys.stdin.readline

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    # return int(num) + 1 if num - int(num) >= 0.5 else int(num)

n = int(input())
if n:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    exc = my_round(n * 0.15)
    print(my_round(sum(arr[exc:-exc] if exc else arr) / (n - 2 * exc)))
else:
    print(0)