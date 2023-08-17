a = input()

r = 0
for i in range(len(a)):
    k = a[i]
    if k in ['A', 'B', 'C']:
        r += 3
    elif k in ['D', 'E', 'F']:
        r += 4
    elif k in ['G', 'H', 'I']:
        r += 5
    elif k in ['J', 'K', 'L']:
        r += 6
    elif k in ['M', 'N', 'O']:
        r += 7
    elif k in ['P', 'Q', 'R', 'S']:
        r += 8
    elif k in ['T', 'U', 'V']:
        r += 9
    elif k in ['W', 'X', 'Y', 'Z']:
        r += 10

print(r)