import sys

n = int(input())
stu = list(map(int, input().split()))

stack = []
tg = 1

for i in stu:
    stack.append(i)
    while stack and stack[-1] == tg:
        stack.pop()
        tg += 1
    if len(stack) > 1 and stack[-1] > stack[-2]:
        print("Sad")
        sys.exit()

if stack:
	print("Sad")
else:
	print("Nice")