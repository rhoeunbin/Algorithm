score = []
for i in range(8):
    score.append(int(input()))

ans = 0
temp = []
for i in range(5):
    ans += max(score)
    temp.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = 0
temp.sort()
print(ans)
print(*temp)