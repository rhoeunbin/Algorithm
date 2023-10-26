n = int(input())
x_value = []
y_value = []
for i in range(n):
    x, y = map(int,input().split())
    x_value.append(x)
    y_value.append(y)
print((max(x_value) - min(x_value)) * (max(y_value) - min(y_value)))