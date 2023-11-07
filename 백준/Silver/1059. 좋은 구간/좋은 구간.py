l = int(input())
s = list(map(int, input().split()))
n = int(input())

# (10보다 작은 수의 개수) * (10을 포함한 10보다 큰 수의 개수) + (10보다 큰 수의 개수)
s.sort()
if n in s:
    print(0)
else:
    min_v, max_v = 0, 0
    for num in s:
        if num < n:
            min_v = num
        elif num > n and max_v == 0:
            max_v = num
    max_v -= 1
    min_v += 1    
    print((n - min_v)*(max_v - n + 1) + (max_v - n))