from itertools import permutations

n = int(input())
num_list = [i for i in range(1, n+1)]

for nums in list(permutations(num_list)):
    for num in nums:
        print(num, end=' ')
    print()