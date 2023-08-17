a = input()

for i in range(len(a)):
    if a[i] != a[-i-1]:
        k = 0
        break
    else:
        k = 1
if k == 0:
    print('0')
else:
    print('1')

