n = input()
cnt = [0] * 10
for x in n:
    idx = int(x)
    if idx == 9:
        idx = 6
    cnt[idx] += 1
cnt[6] = (cnt[6] + 1) // 2
print(max(cnt))