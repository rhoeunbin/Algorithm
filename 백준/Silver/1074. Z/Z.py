N, r, c = map(int, input().split()) # r행 c열을 몇 번째로 방문했는지
ans = 0


while N != 0: 
		N -= 1 # 배열의 크기를 계속 줄여감
		size = 2 ** N
		# 1사분면
		if r < size and c < size:
				ans += 0

		# 2사분면
		elif r < size and c >= size: 
				ans += size * size * 1
				c -= size
					
		# 3사분면    
		elif r >= size and c < size: 
				ans += size * size * 2
				r -= size
					
		# 4사분면    
		else:
				ans += size * size * 3
				r -= size
				c -= size
print(ans)