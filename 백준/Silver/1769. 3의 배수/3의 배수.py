x = input()

cnt = 0
while int(x) >= 10:
    th = 0
    for i in range(len(x)):
        th += int(x[i])
    x = str(th)
    cnt += 1
print(cnt)
if int(x) % 3 == 0:
    print('YES')
else:
    print('NO')