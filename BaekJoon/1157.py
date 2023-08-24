a = input()

def max_item(data):
    count_list=[]
    for i in data:
        count_list.append(data.count(i))
    return data[count_list.index(max(count_list))]


if len(a)==1:
    if ord(a) >= 97:
        print(chr(ord(a)-32))
    else:
        print(a)
else:    
    l = []
    for i in range(len(a)):
        if ord(a[i])>=97:
            l.append(chr(ord(a[i])-32))
        else:
            l.append(a[i])

        
    r = []

    r.append(max_item(l))
    l.remove(max_item(l))
    r.append(max_item(l))

    if r[0]!=r[1]:
        print('?')
    else:
        print(r[0])
