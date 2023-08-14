a = input()
r = [-1 * 1 for i in range(26)]
for i in a[::-1]:
    r.insert(ord(i)-97, a.index(i))
    r.pop(ord(i)-96)
    
for i in r:
    print(i, end=" ")