t = int(input())

for _ in range(t):
    left = []
    right = []
    pwd = input()

    for i in pwd:
        if i == '-':
            if left:
                left.pop()
        elif i == '<': # 왼쪽 스택에 있는 문자 오른쪽 스택으로
            if left:
                right.append(left.pop())
        elif i == '>': # 오른쪽 스택에 있는 문자 왼쪽 스택으로
            if right:
                left.append(right.pop())
        else:
            left.append(i)
            
    while right:
        left.append(right.pop())

    print("".join(left))