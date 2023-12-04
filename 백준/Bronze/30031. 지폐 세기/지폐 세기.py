ans = 0
for _ in range(int(input())):
    row, col = map(int, input().split())

    if row == 136:
        ans += 1000
    elif row == 142:
        ans += 5000
    elif row == 148:
        ans += 10000
    elif row == 154:
        ans += 50000
print(ans)