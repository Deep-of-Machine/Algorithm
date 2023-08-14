n, m = map(int, input().split())

a = []
b = []
for i in range(n):
    k = list(map(int, input().split()))
    a.append(k)

for i in range(n):
    k = list(map(int, input().split()))
    b.append(k)

for i, j in zip(a, b):
    for k in range(m):
        print(i[k] + j[k], end=" ")
    print()