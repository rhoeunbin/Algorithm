for _ in range(int(input())):
    n = int(input())
    b = bin(n)[2:]
    for i in range(len(b)):
        if b[-i - 1] == '1':
            print(i, end = ' ')