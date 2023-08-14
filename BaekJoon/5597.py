a = [1 * i for i in range(1, 31)]

for i in range(28):
    k = int(input())
    a.remove(k)

for i in a:
    print(i)