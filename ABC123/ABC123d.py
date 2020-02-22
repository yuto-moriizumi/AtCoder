x, y, z, k = map(int, input().split())
a = []
b = []
c = []
for i in input().split():
    a.append(int(i))
for i in input().split():
    b.append(int(i))
for i in input().split():
    c.append(int(i))
for i in range(k):
    if(len(a) != 0):
        maxA = max(a)
        indA = a.index(maxA)
    if(len(b) != 0):
        maxB = max(b)
        indB = b.index(maxB)
    if(len(c) != 0):
        maxC = max(c)
        indC = c.index(maxC)
    ind = (maxA, maxB, maxC).index(max(maxA, maxB, maxC))
    print(a, b, c)
    print(maxA+maxB+maxC)
    if (len(a) != 0 and ind == 0):
        a.remove(maxA)
    elif (len(b) != 0 and ind == 1):
        b.remove(maxB)
    elif (len(c) != 0 and ind == 2):
        c.remove(maxC)
