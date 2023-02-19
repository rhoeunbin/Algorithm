cnt = 0
for i in range(int(input())):
    n = int(input())
    if n == 1:
        cnt += 1
    else:
        cnt -= 1

if cnt > 0:
    print("Junhee is cute!")
else:
  print("Junhee is not cute!")