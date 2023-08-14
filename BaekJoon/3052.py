try:
    s = {}
    for i in range(10):
        a = int(input())
        s.add(a%42)
    print(10-len(s))
except Exception as e:
    print(e)
