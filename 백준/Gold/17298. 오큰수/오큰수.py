n = int(input())
nge = list(map(int, input().split()))

ans = [-1] * n 
stack = [] 
for i in range(n):
    # 만약 스택의 마지막 인덱스의 nge값이 비교값보다 작다면
    # 그 값보다 클 때까지 해당 값을 오큰수로 설정
    while stack and nge[stack[-1]] < nge[i]:
        ans[stack.pop()] = nge[i]
    stack.append(i)  # 해당 인덱스 스택에 넣기

print(*ans)