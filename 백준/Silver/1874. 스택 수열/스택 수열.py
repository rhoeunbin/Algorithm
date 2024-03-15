n = int(input())
stack = []
ans = []
temp = True
cnt = 1

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        temp = False

if not temp:
    print('NO')
else:
    for i in ans:
        print(i)