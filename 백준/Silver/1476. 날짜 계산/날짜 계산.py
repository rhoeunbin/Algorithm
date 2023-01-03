E, S, M = map(int,input().split())
# 지구를 나타내는 수를 E, 태양을 나타내는 수를 S, 달을 나타내는 수를 M

year = 1

while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        break
    year += 1

print(year)
