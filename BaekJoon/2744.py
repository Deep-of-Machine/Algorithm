a = input()

for i in range(len(a)):
    if ord(a[i])>=97:
        print(chr(int(ord(a[i]))-32), end='')
    elif ord(a[i])<97:
        print(chr(int(ord(a[i]))+32), end='')