import sys
import math
input = sys.stdin.readline

for test in range(int(input())):
    decimal = list(map(int, input().split()))
    answer = 0

    for i in range(1, len(decimal)):
        for j in range(i+1, len(decimal)):
            answer += math.gcd(decimal[i],decimal[j])
        
    print(answer)