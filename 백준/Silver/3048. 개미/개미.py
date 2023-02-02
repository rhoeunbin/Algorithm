n1, n2 = map(int,input().split())

a1 = list(input())
a2 = list(input())

t = int(input())

road = a1[::-1] + a2

# print(road)
for i in range(t):
    for j in range(len(road) - 1):
        if road[j] in a1 and road[j + 1] in a2:
            road[j], road[j + 1] = road[j + 1], road[j]
            # print(road)
            if road[j + 1] == a1[0]:
                break

print(''.join(road))