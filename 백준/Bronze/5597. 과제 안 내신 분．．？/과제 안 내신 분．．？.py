stu = []
for _ in range(28):
    stu.append(int(input()))
stu.sort()
for i in range(1, 31):
    if i not in stu:
        print(i)