N = int(input())
# 자기보다 큰 사람 몇 명 이었는지 기억 정보
## 키 작은 사람부터 자기 왼쪽에 큰 사람 몇 명 있었는지
watch = list(map(int, input().split()))
# 키 큰 사람부터 insert 시키기 위해
watch.reverse()

stand = []
for i in range(N):
    # insert(i, x) : i 위치에 x 추가
    stand.insert(watch[i], N-i)
print(*stand)