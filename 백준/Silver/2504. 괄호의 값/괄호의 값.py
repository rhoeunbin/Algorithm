gwalho = list(input())
stack = []
cal = 1
ans = 0

for i in range(len(gwalho)):
    if gwalho[i] == '(':
        stack.append(gwalho[i])
        cal *= 2
    elif gwalho[i] == '[':
        stack.append(gwalho[i])
        cal *= 3
    elif gwalho[i] == ')':
      if not stack or stack[-1] == '[':
          ans = 0
          break
      if gwalho[i - 1] == '(':
          ans += cal
      stack.pop()
      cal //= 2   # 이미 앞에서 *2를 했으니깐

    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if gwalho[i-1] == "[":
            ans += cal

        stack.pop()
        cal //= 3 # 이미 앞에서 *3을 했으니까

if stack: # 입력이 올바르지 못한 괄호열이면 반드시 0
    print(0) 
else: # 입력이 올바르면 계산값 구하기
    print(ans)