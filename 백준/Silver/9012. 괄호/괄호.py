n = int(input())

for i in range(n):
    gwal = input()
    stack = []
    for i in gwal:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')