score = 0
for i in range(5):
    stu = int(input())
    if stu < 40:
        stu = 40
    
    score += stu

print(score//5)
    