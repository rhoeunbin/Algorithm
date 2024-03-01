n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

for i in arr2:
    if i in arr:
        print(1)
    else:
        print(0)