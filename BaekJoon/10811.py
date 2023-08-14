n, m = map(int, input().split())

b = [1 * i for i in range(1, n+1)]
c = []
for k in range(m):
    i, j = map(int, input().split())
    if i < j:
        for l in range(j-i+1):
            c.append(b[i-1])
            b.pop(i-1)
        for l in range(j-i+1):
            b.insert(i-1, c[0])
            c.pop(0)
    if i > j:
        for l in range(i-j+1):
            c.append(b[j-1])
            b.pop(j-1)
        for l in range(i-j+1):
            b.insert(j-1, c[0])
            c.pop(0)
    else:
        pass

for i in b:
    print(i, end=" ")