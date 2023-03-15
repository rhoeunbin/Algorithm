word = input()
bomb = list(input())

stack = []

for i in range(len(word)):
    stack.append(word[i])
    if stack[-len(bomb):] == bomb:
        del stack[-len(bomb):] 

if stack: 
    print(*stack, sep='')
else: 
    print("FRULA")