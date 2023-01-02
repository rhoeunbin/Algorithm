a = int(input()) #개수
nums = list(map(int,input().split()))
nums.sort()
print(nums[0] * nums[-1]) 