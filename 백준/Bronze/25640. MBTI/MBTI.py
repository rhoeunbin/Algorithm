me = input()
cnt = 0
for i in range(int(input())):
    you = input()
    if you == me:
        cnt += 1
print(cnt)