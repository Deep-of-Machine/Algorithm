total = int(input())
count = int(input())

result = 0
for i in range(count):
    a, b = map(int, input().split())
    calc = a * b
    result += calc

if total == result:
    print('Yes')
else:
    print('No')