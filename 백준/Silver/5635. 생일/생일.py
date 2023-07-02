n = int(input())
birth = []

for i in range(n):
    name, d, m, y = input().split()
    birth.append((int(y), int(m), int(d), name))
    # print(birth)
birth.sort()
print(birth[-1][3])
print(birth[0][3])