a = int(input()) # n의 진짜 약수의 개수
nums = list(map(int,input().split())) # n의 진짜 약수
print(max(nums)*min(nums)) # nums리스트에서 작은 값 * 큰 값