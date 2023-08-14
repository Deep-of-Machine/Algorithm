n, m = map(int, input().split())

b = [1 * i for i in range(1, n+1)]

l = []

for i in range(m):
    l=[]
    q,w = map(int, input().split())
    if q > w:
        print(b[w:q+1])
    elif q < w :
        print(b[q:w+1])
    else:
        pass