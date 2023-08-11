b, c = map(int, input().split())
a = [0 * i for i in range(b)]

for r in range(c):
    i, j, k = map(int, input().split())
    for l in range(j-i+1):
        a.pop(i-1)
        a.insert(i-1, k)
        i+=1
    
for i in a:
    print(i, end=" ")