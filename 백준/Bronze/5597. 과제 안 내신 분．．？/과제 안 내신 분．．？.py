students = [i for i in range(1,31)]

for _ in range(28):
    apply = int(input())
    students.remove(apply) #소거

print(min(students))
print(max(students))