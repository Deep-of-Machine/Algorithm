a = int(input())
b = list(input().split())
c = int(input())
result = 0
for i in range(a):
    if int(b[i]) == c:
        result += 1
print(result)