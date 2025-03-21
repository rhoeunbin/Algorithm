n = input()
length = len(n) - 1
ans = 0

for i in range(length):
    ans += 9 * (10**i) * (i+1)
    
ans += ((int(n) - (10 ** length))+1) * (length+1)

print(ans)