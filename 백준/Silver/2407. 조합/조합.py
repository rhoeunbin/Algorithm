import math

n, m = map(int,input().split())

top = math.factorial(n)
bottom = math.factorial(m) * math.factorial(n-m)
print(top//bottom)

'''
nCm = n!/m!(n-m)!
'''