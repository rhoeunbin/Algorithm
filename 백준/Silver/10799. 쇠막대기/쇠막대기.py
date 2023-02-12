gwal = list(input())
stack = []
ans = 0

for i in range(len(gwal)):
    if gwal[i] == '(':
        stack.append(gwal[i])
    else:
        if gwal[i - 1] == '(': # ')'가 나오고 이전 문자가 '('이었다면 해당 파트는 레이저
            stack.pop()
            ans += len(stack) # 현재 stack에 쌓인 '('개수(=쇠막대기 개수)만큼 개수를 더해준다.
        else: # ')'가 나오고 이전 문자도 ')'이었다면
            stack.pop()
            ans += 1 # 하나가 나올때마다 하나씩만 추가

print(ans)