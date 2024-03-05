import sys
input = sys.stdin.readline

word = list(input().rstrip())
ans = []

for _ in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'L':
        if word:
              ans.append(word.pop())
              
    elif cmd[0] == 'D':
        if ans:
            word.append(ans.pop())

    elif cmd[0] == 'B':
        if word:
            word.pop()
              
    else:
        word.append(cmd[1])
        
word.extend(reversed(ans))
print(''.join(word))