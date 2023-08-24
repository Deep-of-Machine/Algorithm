n = int(input())

def remove_p(s):
    string = []
    prev=None

    for i in s:
        if prev != i:
            string.append(i)
            prev = i
    
    return "".join(string)

r = []

for i in range(n):
    a = input()
    t = remove_p(a)
    tt = set(t)

    if len(t)==len(tt):
        r.append(t)
    

print(len(r))