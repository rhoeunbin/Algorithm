ans = []
while True:
    n = int(input())
    if n == 0:
        break
    stu = []
    for i in range(n):
        stu.append(input())

    stack = []
    for i in range(2 * n - 1):
        num, ab = input().split()
        if num in stack:
            stack.remove(num)
        else:
            stack.append(num)

    ans.append(stu[int(stack[0]) - 1])

for idx, v in enumerate(ans):
    print(idx + 1, v)