n = int(input())
l = list(map(int, input().split()))
c = 0
for i in l:
    c += (i/max(l)*100)

print(c/n)