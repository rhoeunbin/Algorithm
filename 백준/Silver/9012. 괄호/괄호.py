t = int(input())

for _ in range(t):
    stack = []
    paren = input()

    for i in paren:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:  
            print('YES')
        else :
            print('NO')