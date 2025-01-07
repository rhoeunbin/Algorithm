k = int(input())
for j in range(k):
    num = list(map(int, input().split()))
    n, c = num[0], sorted(num[1:])
    Max = c[-1]
    Min = c[0]
    gap = max((c[i + 1] - c[i]) for i in range(n - 1)) 
    print("Class", j + 1)
    print(f"Max {Max}, Min {Min}, Largest gap {gap}")