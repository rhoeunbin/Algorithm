word = list(input())
n = len(word)
stack = []
m = int(input())

for i in range(m):
    command = input().split()
# print(command)
    if command[0] == 'L' and word:
        stack.append(word.pop())
        
    elif command[0] == 'D' and stack:
        word.append(stack.pop())
        
    elif command[0] == 'B' and word:
        word.pop()
        
    elif command[0] == 'P':
        word.append(command[1])

ans = word + stack[::-1]
print(''.join(ans))       