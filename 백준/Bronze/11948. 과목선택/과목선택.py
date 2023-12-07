data = []

for _ in range(6) :
  data.append(int(input()))

value1 = sorted(data[:4])
value2 = data[4:]

print(sum(value1[1:]) + max(value2))