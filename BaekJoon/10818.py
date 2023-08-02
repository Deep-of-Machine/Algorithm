a = int(input())
b = list(input().split())
c =[]
for i in b:
    c.append(int(i))

print(min(c), max(c))