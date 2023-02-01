t =int(input())

for i in range(t):
    stack = []
    paren = input()  

    for j in paren:
        if j == '(':
            stack.append(j)  
        elif j == ')': 
            if stack :
                stack.pop()
            else :
                print('NO') 
                break   
    else:
        if not stack:  
            print('YES')
        else :
            print('NO')