mario = []
score = 0

for _ in range(10):
    mario.append(int(input()))
for i in mario:
    score += i
    if score >= 100:
        if score - 100 > 100 - (score - i):
            score -= i
        break
print(score)