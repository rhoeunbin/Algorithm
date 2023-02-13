n = int(input())
h = []
stack = []
ans = 0

for i in range(n):
    h.append(int(input()))

    while stack and stack[-1] <= h[i]: 
        # print(stack)
        stack.pop() # 지우기
    stack.append(h[i])
    # print(stack)
    ans += len(stack) - 1

print(ans)
