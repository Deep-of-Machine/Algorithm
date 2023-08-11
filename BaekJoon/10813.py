N, M = map(int, input().split())

li = [1 * i for i in range(1, N+1)]

for k in range(M):
    i, j = map(int, input().split())
    if i == j:
        pass
    else:
        r = li[j-1]
        l = li[i-1]
        li.pop(j-1)
        li.pop(i-1)
        li.insert(i-1, r)
        li.insert(j-1, l)

for i in li:
    print(i, end=" ")