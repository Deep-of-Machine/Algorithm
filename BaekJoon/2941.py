li = 'dz='
l = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

k = input()
for q in range(len(k)):
    for i in l:
        if i in k and li in k:
            k = k.replace(li, 'a')
        elif i in k:
            k = k.replace(i, 'a')
    
print(len(k))