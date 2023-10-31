ao, az = map(int, input().split())
c = int(input())
n = int(input())

if (ao * n + az <= c * n) and ao <= c:
    print(1)
else:
    print(0)