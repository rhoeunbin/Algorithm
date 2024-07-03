n = int(input())
cnt, start, end = 1, 1, 1
hop= 1

while end != n:
    if hop == n:
        cnt += 1
        end += 1
        hop += end
    elif hop > n:
        hop -= start
        start += 1
    else:
        end += 1
        hop += end
print(cnt)