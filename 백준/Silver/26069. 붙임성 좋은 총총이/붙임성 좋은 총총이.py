n = int(input())

dance =  {"ChongChong"}
for i in range(n):
    a, b = input().split()
    
    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)
print(len(dance))